from app.database import engine, Base
from app.models import Angel, Saint

Base.metadata.create_all(bind=engine)
print("Teblelas criadas com sucesso!")
