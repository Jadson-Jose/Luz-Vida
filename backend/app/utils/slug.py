import re
from sqlalchemy.orm import Session
from app import models

def gerar_slug_unico(db: Session, titulo: str, item_id: int = None) -> str:
    titulo = titulo.lower()
    
    # Remove acentos comuns
    acentos = {
        'á':'a', 'à':'a', 'â':'a', 'ã':'a', 'ä':'a',
        'é':'e', 'è':'e', 'ê':'e', 'ë':'e',
        'í':'i', 'ì':'i', 'î':'i', 'ï':'i',
        'ó':'o', 'ò':'o', 'ô':'o', 'õ':'o', 'ö':'o',
        'ú':'u', 'ù':'u', 'û':'u', 'ü':'u',
        'ç':'c', 'ñ':'n'
    }
    for k, v in acentos.items():
        titulo = titulo.replace(k, v)
    
    # Remove caracteres especiais e substitui espaços por hífen
    slug = re.sub(r'[^a-z0-9\s-]', '', titulo)
    slug = re.sub(r'\s+', '-', slug).strip('-')
    
    # Garante que o slug seja único no banco
    slug_base = slug
    contador = 1
    while True:
        query = db.query(models.ChurchContent).filter(models.ChurchContent.slug == slug)
        if item_id:
            query = query.filter(models.ChurchContent.id != item_id)
        if not query.first():
            return slug
        
        slug = f"{slug_base}-{contador}"
        contador += 1