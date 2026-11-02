from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app import models, schemas
from app.auth import require_admin

router = APIRouter(prefix="/api/church", tags=["church"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{category}", response_model=List[schemas.ChurchContentOut])
def list_by_category(category: str, db: Session = Depends(get_db)):
    items = db.query(models.ChurchContent).filter(models.ChurchContent.category == category).order_by(models.ChurchContent.order).all()
    return items

@router.get("/topic/{id}", response_model=schemas.ChurchContentOut)
def get_topic(id: int, db: Session = Depends(get_db)):
    item = db.query(models.ChurchContent).filter(models.ChurchContent.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado.")
    return item

# Rota para você criar o conteúdo pelo Swagger (protegida)
@router.post("/", response_model=schemas.ChurchContentOut, dependencies=[Depends(require_admin)])
def create_church_content(item: schemas.ChurchContentCreate, db: Session = Depends(get_db)):
    db_item = models.ChurchContent(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item