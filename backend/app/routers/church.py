from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app import models, schemas
from app.auth import require_admin
from app.utils.slug import gerar_slug_unico  # <-- IMPORT ADICIONADO

router = APIRouter(prefix="/api/church", tags=["church"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{category}", response_model=List[schemas.ChurchContentOut])
def list_by_category(category: str, db: Session = Depends(get_db)):
    items = db.query(models.ChurchContent).filter(
        models.ChurchContent.category == category
    ).order_by(models.ChurchContent.order).all()
    return items


@router.get("/topic/{slug}", response_model=schemas.ChurchContentOut)
def get_topic_by_slug(slug: str, db: Session = Depends(get_db)):
    item = db.query(models.ChurchContent).filter(models.ChurchContent.slug == slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado.")
    return item


@router.post("/", response_model=schemas.ChurchContentOut, dependencies=[Depends(require_admin)])
def create_church_content(item: schemas.ChurchContentCreate, db: Session = Depends(get_db)):
    db_item = models.ChurchContent(**item.dict())
    db_item.slug = gerar_slug_unico(db, item.title)  # <-- GERA O SLUG
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.put("/{id}", response_model=schemas.ChurchContentOut, dependencies=[Depends(require_admin)])
def update_church_content(id: int, updated: schemas.ChurchContentCreate, db: Session = Depends(get_db)):
    item = db.query(models.ChurchContent).filter(models.ChurchContent.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado.")

    # Se o título mudou, gera um novo slug
    if item.title != updated.title:
        item.slug = gerar_slug_unico(db, updated.title, item_id=id)

    for key, value in updated.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_church_content(id: int, db: Session = Depends(get_db)):
    item = db.query(models.ChurchContent).filter(models.ChurchContent.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado.")
    db.delete(item)
    db.commit()