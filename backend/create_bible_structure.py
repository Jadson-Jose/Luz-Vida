from sqlalchemy import text
from app.database import SessionLocal
from app.models import Book, Chapter

# Estrutura da Bíblia Católica (73 livros) com o número de capítulos de cada um
# Baseado no cânon católico (Vulgata)
BIBLE_STRUCTURE = [
    # Antigo Testamento
    ("Gênesis", "Gn", 50),
    ("Êxodo", "Ex", 40),
    ("Levítico", "Lv", 27),
    ("Números", "Nm", 36),
    ("Deuteronômio", "Dt", 34),
    ("Josué", "Js", 24),
    ("Juízes", "Jz", 21),
    ("Rute", "Rt", 4),
    ("1 Samuel", "1Sm", 31),
    ("2 Samuel", "2Sm", 24),
    ("1 Reis", "1Rs", 22),
    ("2 Reis", "2Rs", 25),
    ("1 Crônicas", "1Cr", 29),
    ("2 Crônicas", "2Cr", 36),
    ("Esdras", "Esd", 10),
    ("Neemias", "Ne", 13),
    ("Tobias", "Tb", 14),
    ("Judite", "Jdt", 16),
    ("Ester", "Est", 10),
    ("1 Macabeus", "1Mc", 16),
    ("2 Macabeus", "2Mc", 15),
    ("Jó", "Jó", 42),
    ("Salmos", "Sl", 150),
    ("Provérbios", "Pr", 31),
    ("Eclesiastes", "Ecl", 12),
    ("Cântico dos Cânticos", "Ct", 8),
    ("Sabedoria", "Sb", 19),
    ("Eclesiástico", "Eclo", 51),
    ("Isaías", "Is", 66),
    ("Jeremias", "Jr", 52),
    ("Lamentações", "Lm", 5),
    ("Baruc", "Br", 6),
    ("Ezequiel", "Ez", 48),
    ("Daniel", "Dn", 14),
    ("Oseias", "Os", 14),
    ("Joel", "Jl", 3),
    ("Amós", "Am", 9),
    ("Abdias", "Ab", 1),
    ("Jonas", "Jn", 4),
    ("Miqueias", "Mq", 7),
    ("Naum", "Na", 3),
    ("Habacuc", "Hab", 3),
    ("Sofonias", "Sf", 3),
    ("Ageu", "Ag", 2),
    ("Zacarias", "Zc", 14),
    ("Malaquias", "Ml", 3),
    # Novo Testamento
    ("Mateus", "Mt", 28),
    ("Marcos", "Mc", 16),
    ("Lucas", "Lc", 24),
    ("João", "Jo", 21),
    ("Atos dos Apóstolos", "At", 28),
    ("Romanos", "Rm", 16),
    ("1 Coríntios", "1Cor", 16),
    ("2 Coríntios", "2Cor", 13),
    ("Gálatas", "Gl", 6),
    ("Efésios", "Ef", 6),
    ("Filipenses", "Fl", 4),
    ("Colossenses", "Cl", 4),
    ("1 Tessalonicenses", "1Ts", 5),
    ("2 Tessalonicenses", "2Ts", 3),
    ("1 Timóteo", "1Tm", 6),
    ("2 Timóteo", "2Tm", 4),
    ("Tito", "Tt", 3),
    ("Filemon", "Fm", 1),
    ("Hebreus", "Hb", 13),
    ("Tiago", "Tg", 5),
    ("1 Pedro", "1Pd", 5),
    ("2 Pedro", "2Pd", 3),
    ("1 João", "1Jo", 5),
    ("2 João", "2Jo", 1),
    ("3 João", "3Jo", 1),
    ("Judas", "Jd", 1),
    ("Apocalipse", "Ap", 22),
]

def create_structure():
    with SessionLocal() as db:
        # Limpar livros e capítulos existentes (mantém anjos e santos)
        print("Limpando livros e capítulos existentes...")
        db.execute(text("DELETE FROM verses"))
        db.execute(text("DELETE FROM chapters"))
        db.execute(text("DELETE FROM books"))
        db.execute(text("ALTER SEQUENCE verses_id_seq RESTART WITH 1"))
        db.execute(text("ALTER SEQUENCE chapters_id_seq RESTART WITH 1"))
        db.execute(text("ALTER SEQUENCE books_id_seq RESTART WITH 1"))
        db.commit()

        total_chapters = 0
        for name, abbrev, num_chapters in BIBLE_STRUCTURE:
            book = Book(name=name, abbreviation=abbrev)
            db.add(book)
            db.flush()

            for chapter_num in range(1, num_chapters + 1):
                chapter = Chapter(number=chapter_num, book_id=book.id)
                db.add(chapter)
                total_chapters += 1

            db.commit()
            print(f"  {name} ({num_chapters} capítulos)")

        print(f"\nEstrutura criada: {len(BIBLE_STRUCTURE)} livros, {total_chapters} capítulos.")
        print("Agora edite os versículos pelo painel administrativo.")

if __name__ == "__main__":
    create_structure()
