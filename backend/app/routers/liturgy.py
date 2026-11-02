from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/api/liturgy", tags=["liturgy"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/today", response_model=schemas.DailyReadingOut)
def get_today_liturgy(db: Session = Depends(get_db)):
    today = date.today()
    # Busca a liturgia de hoje
    reading = db.query(models.DailyReading).filter(models.DailyReading.date == today).first()
    
    if not reading:
        # Se não tiver a de hoje, pega a mais recente (fallback para testes)
        reading = db.query(models.DailyReading).filter(models.DailyReading.date <= today).order_by(models.DailyReading.date.desc()).first()
        
    if not reading:
        raise HTTPException(status_code=404, detail="Nenhuma liturgia cadastrada.")
    return reading