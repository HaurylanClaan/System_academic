import sqlite3

conn = sqlite3.connect("sistema_academico.db")
cursor = conn.cursor()

# Alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    identidade TEXT NOT NULL,
    nascimento TEXT NOT NULL,
    nome_mae TEXT NOT NULL,
    nome_pai TEXT NOT NULL
);

""")

# Professores
cursor.execute("""
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    identidade TEXT NOT NULL,
    nascimento TEXT NOT NULL,
    materia TEXT NOT NULL
);

""")

# Disciplinas
cursor.execute("""
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL
);

""")

# Notas
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    disciplina_id INTEGER NOT NULL,
    nota REAL NOT NULL,
    UNIQUE(aluno_id, disciplina_id),
    FOREIGN KEY(aluno_id) REFERENCES alunos(id),
    FOREIGN KEY(disciplina_id) REFERENCES disciplinas(id)
);

""")

conn.commit()
conn.close()

print("Banco de dados 'sistema_academico.db' criado com sucesso!")
