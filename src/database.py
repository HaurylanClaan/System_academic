import sqlite3

DB_PATH = "sistema_academico.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nome_normalizado TEXT NOT NULL UNIQUE,
        identidade TEXT NOT NULL UNIQUE,
        nascimento TEXT NOT NULL,
        nome_mae TEXT NOT NULL,
        nome_pai TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL UNIQUE
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL,
        disciplina_id INTEGER NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL,
        media REAL,
        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
    );
    """)

    conn.commit()
    conn.close()

# DISCIPLINAS
def carregar_disciplinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, codigo FROM disciplinas")
    disciplinas = cursor.fetchall()
    conn.close()
    return disciplinas

def salvar_disciplina(nome, codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO disciplinas (nome, codigo) VALUES (?, ?)", (nome, codigo))
    conn.commit()
    conn.close()

def excluir_disciplina(nome, codigo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM disciplinas WHERE nome = ? AND codigo = ?", (nome, codigo))
    conn.commit()
    conn.close()

# ALUNOS
def carregar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, identidade, nascimento, nome_mae, nome_pai FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def excluir_aluno(identidade):
    conn = conectar()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE identidade = ?", (identidade,))
        conn.commit()
    finally:
        conn.close()

#criar notas
from calculo_media import calcular_media  # ← importar a função

def salvar_nota(aluno_id, disciplina_id, nota1, nota2):
    media = calcular_media(nota1, nota2)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO notas (aluno_id, disciplina_id, nota1, nota2, media)
        VALUES (?, ?, ?, ?, ?)
    """, (aluno_id, disciplina_id, nota1, nota2, media))
    conn.commit()
    conn.close()

#ver notas dos alunos
def carregar_alunos_com_id():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def carregar_notas_por_aluno(aluno_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.nome, n.nota1, n.nota2, n.media
        FROM notas n
        JOIN disciplinas d ON n.disciplina_id = d.id
        WHERE n.aluno_id = ?
    """, (aluno_id,))
    notas = cursor.fetchall()
    conn.close()
    return notas




    conn.commit()
    conn.close()
