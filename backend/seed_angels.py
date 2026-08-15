from app.database import SessionLocal
from app.models import Angel

angels_data = [
    {
        "name": "São Miguel Arcanjo",
        "title": "Príncipe da Milícia Celeste",
        "icon": "shield",
        "short_text": 'Seu nome significa "Quem como Deus?" — o brado de fidelidade que ecoou contra a revolta de Lúcifer.',
        "full_text": 'São Miguel Arcanjo é o líder dos exércitos celestiais e o protetor da Igreja. Seu nome, "Quem como Deus?", é um grito de humildade e fidelidade diante da soberba de Lúcifer. Ele é mencionado no Apocalipse como aquele que combate o dragão, e na tradição católica é invocado contra as ciladas do maligno. É padroeiro dos soldados, dos policiais e de todos os que defendem a fé. Sua festa é celebrada em 29 de setembro, junto com os arcanjos Gabriel e Rafael.',
    },
    {
        "name": "São Gabriel Arcanjo",
        "title": "Mensageiro da Anunciação",
        "icon": "lily",
        "short_text": 'O anjo que trouxe a Maria o anúncio da encarnação do Verbo: "Ave, cheia de graça."',
        "full_text": 'São Gabriel é o arcanjo mensageiro por excelência. Seu nome significa "Força de Deus". Ele apareceu ao profeta Daniel, anunciou a Zacarias o nascimento de João Batista e, sobretudo, trouxe a Maria o anúncio da encarnação do Filho de Deus. É padroeiro dos comunicadores, dos correios e de todos os que transmitem mensagens importantes. Sua festa é celebrada em 29 de setembro, junto com Miguel e Rafael.',
    },
    {
        "name": "São Rafael Arcanjo",
        "title": "Médico de Deus",
        "icon": "fish",
        "short_text": 'Guiou o jovem Tobias e devolveu a visão a seu pai — seu nome significa "Deus cura".',
        "full_text": 'São Rafael é o arcanjo da cura e companheiro de viagem. No Livro de Tobias, ele acompanha o jovem Tobias, protegendo-o e curando a cegueira de seu pai. Seu nome significa "Deus cura". É padroeiro dos viajantes, dos enfermos, dos médicos e dos farmacêuticos. Sua festa é celebrada em 29 de setembro, junto com Miguel e Gabriel.',
    },
    {
        "name": "Anjo da Guarda",
        "title": "Companheiro de Cada Dia",
        "icon": "wing",
        "short_text": "A cada pessoa foi confiado um anjo que a acompanha, protege e intercede desde o nascimento.",
        "full_text": "A Igreja ensina que cada pessoa tem um anjo da guarda desde o nascimento. Esse anjo nos ilumina, nos protege e intercede por nós diante de Deus. A memória dos Santos Anjos da Guarda é celebrada em 2 de outubro. A devoção ao anjo da guarda é antiga e sempre incentivada pela Igreja como sinal da providência divina.",
    },
    {
        "name": "Os Nove Coros Angelicais",
        "title": "A Hierarquia Celeste",
        "icon": "rings",
        "short_text": "Serafins, Querubins, Tronos, Dominações, Virtudes, Potestades, Principados, Arcanjos e Anjos.",
        "full_text": "A tradição, sistematizada por Pseudo-Dionísio Areopagita, descreve nove coros angelicais divididos em três hierarquias: Serafins, Querubins e Tronos (primeira hierarquia); Dominações, Virtudes e Potestades (segunda); Principados, Arcanjos e Anjos (terceira). Cada coro tem uma missão específica na ordem da criação e na adoração divina.",
    },
    {
        "name": "Anjos na Sagrada Escritura",
        "title": "Presença nas Escrituras",
        "icon": "flame",
        "short_text": "Do Éden ao Apocalipse, os anjos anunciam, protegem, louvam e executam a vontade divina.",
        "full_text": 'Ao longo de toda a Bíblia, os anjos aparecem como mensageiros de Deus: fecham o Éden, anunciam a Abraão, guiam o povo no deserto, alimentam Elias, anunciam o nascimento e a ressurreição de Cristo, e no Apocalipse cantam eternamente o "Santo, Santo, Santo". Eles são testemunhas da ação divina na história da salvação.',
    },
]

db = SessionLocal()
for data in angels_data:
    # Verifica se já existe um anjo com o mesmo nome
    existing = db.query(Angel).filter(Angel.name == data["name"]).first()
    if not existing:
        angel = Angel(**data)
        db.add(angel)
db.commit()
db.close()
print("Anjos inseridos com sucesso!")
