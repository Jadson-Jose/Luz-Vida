from app.database import SessionLocal
from app.models import Saint

local_images = {
    "São Francisco de Assis": "/images/saints/francisco.jpg",
    "Santa Teresa de Ávila": "/images/saints/teresa.jpg",
    "São Bento de Núrsia": "/images/saints/bento.jpg",
}

db = SessionLocal()
for name, image_url in local_images.items():
    saint = db.query(Saint).filter(Saint.name == name).first()
    if saint:
        saint.image_url = image_url
        print(f"Imagem local definida para {name}")
db.commit()
db.close()
