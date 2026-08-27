from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.database import SessionLocal

router = APIRouter(prefix="/api", tags=["stats"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    return {
        "books": db.query(models.Book).count(),
        "chapters": db.query(models.Chapter).count(),
        "verses": db.query(models.Verse).count(),
        "angels": db.query(models.Angel).count(),
        "saints": db.query(models.Saint).count(),
    }
