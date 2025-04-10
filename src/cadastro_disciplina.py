from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3
import re  # Para validação de nome com acentos

class CadastroDisciplinaWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback
        self.setWindowTitle("Cadastro de Disciplina")

        # Cria a tabela no banco de dados, se não existir
        self.criar_tabela_disciplinas()

        # Campos de entrada
        self.nome_input = QLineEdit()
        self.codigo_input = QLineEdit()

        # Botões
        self.salvar_btn = QPushButton("Salvar")
        self.cancelar_btn = QPushButton("Cancelar")

        # Conexões
        self.salvar_btn.clicked.connect(self.salvar_disciplina)
        self.cancelar_btn.clicked.connect(self.close)

        # Enter para navegação
        self.nome_input.returnPressed.connect(self.codigo_input.setFocus)
        self.codigo_input.returnPressed.connect(self.salvar_disciplina)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome da Disciplina:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Código da Disciplina (apenas números):"))
        layout.addWidget(self.codigo_input)

        botoes = QHBoxLayout()
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(self.cancelar_btn)
        layout.addLayout(botoes)

        self.setLayout(layout)

    def criar_tabela_disciplinas(self):
        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS disciplinas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    codigo TEXT NOT NULL UNIQUE
                )
            """)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", f"Erro ao criar tabela: {str(e)}")

    def salvar_disciplina(self):
        nome = self.nome_input.text().strip()
        codigo = self.codigo_input.text().strip()

        # Verifica se campos estão preenchidos
        if not nome or not codigo:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        # Validação do nome com acentos e espaços
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            QMessageBox.warning(self, "Erro", "O nome deve conter apenas letras e acentos.")
            return

        # Validação do código (somente números)
        if not codigo.isdigit():
            QMessageBox.warning(self, "Erro", "O código deve conter apenas números inteiros.")
            return

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            # Verifica se já existe disciplina com o mesmo nome (case-insensitive)
            cursor.execute("SELECT * FROM disciplinas WHERE LOWER(nome) = ?", (nome.lower(),))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", f"A disciplina '{nome}' já está cadastrada.")
                return

            # Verifica se já existe código
            cursor.execute("SELECT * FROM disciplinas WHERE codigo = ?", (codigo,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", f"O código '{codigo}' já está em uso.")
                return

            # Insere a disciplina
            cursor.execute("INSERT INTO disciplinas (nome, codigo) VALUES (?, ?)", (nome, codigo))
            conn.commit()
            conn.close()

            if self.callback:
                self.callback(nome)

            QMessageBox.information(self, "Sucesso", "Disciplina cadastrada com sucesso!")
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
