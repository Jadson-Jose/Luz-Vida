from app.database import engine, SessionLocal, Base
from app.models import DailyReading
from datetime import date

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.query(DailyReading).delete()

nova_liturgia = DailyReading(
    date=date.today(),
    liturgical_color="Verde",
    liturgical_season="Tempo Comum",
    first_reading="Leitura da Primeira Carta de São Paulo aos Coríntios (1Cor 1, 1-3)\n\nPaulo, chamado a ser apóstolo de Jesus Cristo pela vontade de Deus...",
    psalm="Salmo 45\n\nR: O Senhor é meu pastor, nada me faltará.",
    second_reading=None,
    gospel="Evangelho de Jesus Cristo segundo São Mateus (Mt 5, 1-12)\n\nNaquele tempo, vendo Jesus as multidões, subiu ao monte e sentou-se..."
)
db.add(nova_liturgia)
db.commit()
print("Liturgia de teste inserida com sucesso!")
db.close()
