from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3

class CadastroProfessorWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback  # Função para atualizar a lista na tela principal
        self.setWindowTitle("Cadastro de Professor")

        # Campos de entrada
        self.nome_input = QLineEdit()
        self.identidade_input = QLineEdit()
        self.nascimento_input = QLineEdit()
        self.materia_input = QLineEdit()

        # Botões
        self.salvar_btn = QPushButton("Salvar")
        self.cancelar_btn = QPushButton("Cancelar")

        # Conexões
        self.salvar_btn.clicked.connect(self.salvar_professor)
        self.cancelar_btn.clicked.connect(self.close)

        # Tecla Enter para navegar entre os campos e salvar
        self.nome_input.returnPressed.connect(self.identidade_input.setFocus)
        self.identidade_input.returnPressed.connect(self.nascimento_input.setFocus)
        self.nascimento_input.returnPressed.connect(self.materia_input.setFocus)
        self.materia_input.returnPressed.connect(self.salvar_professor)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome Completo:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Número de Identificação:"))
        layout.addWidget(self.identidade_input)
        layout.addWidget(QLabel("Data de Nascimento (AAAA-MM-DD):"))
        layout.addWidget(self.nascimento_input)
        layout.addWidget(QLabel("Matéria que vai Lecionar:"))
        layout.addWidget(self.materia_input)

        botoes = QHBoxLayout()
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(self.cancelar_btn)
        layout.addLayout(botoes)

        self.setLayout(layout)

    def salvar_professor(self):
        # Coleta os dados dos campos
        nome = self.nome_input.text().strip()
        identidade = self.identidade_input.text().strip()
        nascimento = self.nascimento_input.text().strip()
        materia = self.materia_input.text().strip()

        # Validação de campos obrigatórios
        if not all([nome, identidade, nascimento, materia]):
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        # Validação de nome apenas com letras e espaços
        if not nome.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Erro", "O nome deve conter apenas letras.")
            return

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            # Verifica se já existe professor com o mesmo nome (ignorando maiúsculas)
            cursor.execute("SELECT * FROM professores WHERE LOWER(nome) = ?", (nome.lower(),))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Já existe um professor com esse nome.")
                return

            # Insere o professor
            cursor.execute("""
                INSERT INTO professores (nome, identidade, nascimento, materia)
                VALUES (?, ?, ?, ?)
            """, (nome, identidade, nascimento, materia))

            conn.commit()
            conn.close()

            # Callback para atualizar lista se necessário
            if self.callback:
                self.callback(nome)

            QMessageBox.information(self, "Sucesso", "Professor cadastrado com sucesso!")
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
