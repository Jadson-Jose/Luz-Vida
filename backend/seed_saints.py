from app.database import SessionLocal
from app.models import Saint

saints_data = [
    {
        "name": "São Francisco de Assis",
        "title": "Padroeiro dos animais e da ecologia",
        "feast_day": "4 de outubro",
        "short_text": "Fundador da Ordem Franciscana, viveu a pobreza evangélica e o amor a toda criação.",
        "full_text": "São Francisco de Assis nasceu em 1181 na Itália. Após uma juventude marcada por sonhos de glória, converteu-se radicalmente ao Evangelho, despojando-se de todos os bens. Fundou a Ordem dos Frades Menores e a Ordem de Santa Clara. É conhecido por seu amor à natureza, aos pobres e pela paz. Recebeu os estigmas de Cristo em 1224. Foi canonizado em 1228, dois anos após sua morte.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Saint_Francis_of_Assisi_by_Jusepe_de_Ribera.jpg/440px-Saint_Francis_of_Assisi_by_Jusepe_de_Ribera.jpg",
    },
    {
        "name": "Santa Teresa de Ávila",
        "title": "Doutora da Igreja",
        "feast_day": "15 de outubro",
        "short_text": "Mística e reformadora do Carmelo, autora de obras clássicas da espiritualidade cristã.",
        "full_text": "Santa Teresa de Jesus, também conhecida como Teresa de Ávila, nasceu na Espanha em 1515. Entrou para o Carmelo e, após uma profunda conversão, iniciou a reforma da ordem, fundando o Carmelo Descalço. Autora de obras como 'O Livro da Vida', 'Caminho de Perfeição' e 'Castelo Interior', é considerada uma das maiores místicas da Igreja. Foi proclamada Doutora da Igreja em 1970.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Santa_Teresa_de_%C3%81vila.jpg/440px-Santa_Teresa_de_%C3%81vila.jpg",
    },
    {
        "name": "São Bento de Núrsia",
        "title": "Padroeiro da Europa",
        "feast_day": "11 de julho",
        "short_text": "Pai do monasticismo ocidental, autor da Regra que orientou a vida monástica por séculos.",
        "full_text": "São Bento nasceu em Núrsia, na Itália, por volta de 480. Retirou-se para viver como eremita e depois fundou o mosteiro de Monte Cassino. Sua Regra, baseada no 'ora et labora' (reza e trabalha), tornou-se o fundamento do monasticismo ocidental. É celebrado como padroeiro da Europa e modelo de vida comunitária e contemplativa.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Saint_Benedict.jpg/440px-Saint_Benedict.jpg",
    },
]

db = SessionLocal()
for data in saints_data:
    existing = db.query(Saint).filter(Saint.name == data["name"]).first()
    if not existing:
        saint = Saint(**data)
        db.add(saint)
        print(f"Santo {data['name']} inserido.")
    else:
        print(f"Santo {data['name']} já existe.")
db.commit()
db.close()
print("Seed concluído!")
