from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.auth import require_admin


router = APIRouter(prefix="/api/angels", tags=["angels"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.AngelOut])
def list_angels(db: Session = Depends(get_db)):
    return db.query(models.Angel).all()


@router.get("/{angel_id}", response_model=schemas.AngelOut)
def get_angel(angel_id: int, db: Session = Depends(get_db)):
    angel = db.query(models.Angel).filter(models.Angel.id == angel_id).first()
    if not angel:
        raise HTTPException(status_code=404, detail="Anjo não encontrado")
    return angel


@router.post(
    "/", response_model=schemas.AngelOut, dependencies=[Depends(require_admin)]
)
def create_angel(angel: schemas.AngelCreate, db: Session = Depends(get_db)):
    db_angel = models.Angel(**angel.dict())
    db.add(db_angel)
    db.commit()
    db.refresh(db_angel)
    return db_angel


@router.put(
    "/{angel_id}",
    response_model=schemas.AngelOut,
    dependencies=[Depends(require_admin)],
)
def update_angel(
    angel_id: int, updated: schemas.AngelCreate, db: Session = Depends(get_db)
):
    angel = db.query(models.Angel).filter(models.Angel.id == angel_id).first()
    if not angel:
        raise HTTPException(status_code=404, detail="Anjo não encontrado")
    for key, value in updated.dict().items():
        setattr(angel, key, value)
    db.commit()
    db.refresh(angel)
    return angel


@router.delete("/{angel_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_angel(angel_id: int, db: Session = Depends(get_db)):
    angel = db.query(models.Angel).filter(models.Angel.id == angel_id).first()
    if not angel:
        raise HTTPException(status_code=404, detail="Anjo não encontrado")
    db.delete(angel)
    db.commit()
    return None
