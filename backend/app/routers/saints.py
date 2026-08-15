from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.auth import require_admin

router = APIRouter(prefix="/api/saints", tags=["saints"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.SaintOut])
def list_saints(db: Session = Depends(get_db)):
    return db.query(models.Saint).all()


@router.get("/{saint_id}", response_model=schemas.SaintOut)
def get_saint(saint_id: int, db: Session = Depends(get_db)):
    saint = db.query(models.Saint).filter(models.Saint.id == saint_id).first()
    if not saint:
        raise HTTPException(status_code=404, detail="Santo não encontrado")
    return saint


@router.post(
    "/", response_model=schemas.SaintOut, dependencies=[Depends(require_admin)]
)
def create_saint(saint: schemas.SaintCreate, db: Session = Depends(get_db)):
    db_saint = models.Saint(**saint.dict())
    db.add(db_saint)
    db.commit()
    db.refresh(db_saint)
    return db_saint


@router.put(
    "/{saint_id}",
    response_model=schemas.SaintOut,
    dependencies=[Depends(require_admin)],
)
def update_saint(
    saint_id: int, updated: schemas.SaintCreate, db: Session = Depends(get_db)
):
    saint = db.query(models.Saint).filter(models.Saint.id == saint_id).first()
    if not saint:
        raise HTTPException(status_code=404, detail="Santo não encontrado")
    for key, value in updated.dict().items():
        setattr(saint, key, value)
    db.commit()
    db.refresh(saint)
    return saint


@router.delete("/{saint_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_saint(saint_id: int, db: Session = Depends(get_db)):
    saint = db.query(models.Saint).filter(models.Saint.id == saint_id).first()
    if not saint:
        raise HTTPException(status_code=404, detail="Santo não encontrado")
    db.delete(saint)
    db.commit()
    return None
