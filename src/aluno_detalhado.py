from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3
from aluno_detalhado import AlunoDetalhado  # Importa a nova classe com todos os dados

class CadastroAlunoWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback  # Função para atualizar a lista na tela principal
        self.setWindowTitle("Cadastro de Aluno")

        # Criação dos campos de entrada
        self.nome_input = QLineEdit()
        self.identidade_input = QLineEdit()
        self.nascimento_input = QLineEdit()
        self.mae_input = QLineEdit()
        self.pai_input = QLineEdit()

        # Botões
        self.salvar_btn = QPushButton("Salvar")
        self.cancelar_btn = QPushButton("Cancelar")

        # Conexão dos botões com funções
        self.salvar_btn.clicked.connect(self.salvar_aluno)
        self.cancelar_btn.clicked.connect(self.close)

        # Configura atalhos com Enter
        self.nome_input.returnPressed.connect(self.identidade_input.setFocus)
        self.identidade_input.returnPressed.connect(self.nascimento_input.setFocus)
        self.nascimento_input.returnPressed.connect(self.mae_input.setFocus)
        self.mae_input.returnPressed.connect(self.pai_input.setFocus)
        self.pai_input.returnPressed.connect(self.salvar_aluno)

        # Layout da janela
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome Completo:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Número de Identidade:"))
        layout.addWidget(self.identidade_input)
        layout.addWidget(QLabel("Data de Nascimento (AAAA-MM-DD):"))
        layout.addWidget(self.nascimento_input)
        layout.addWidget(QLabel("Nome da Mãe:"))
        layout.addWidget(self.mae_input)
        layout.addWidget(QLabel("Nome do Pai:"))
        layout.addWidget(self.pai_input)

        # Layout para botões
        botoes = QHBoxLayout()
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(self.cancelar_btn)
        layout.addLayout(botoes)

        self.setLayout(layout)

    def salvar_aluno(self):
        # Captura os dados dos campos
        nome = self.nome_input.text().strip()
        identidade = self.identidade_input.text().strip()
        nascimento = self.nascimento_input.text().strip()
        mae = self.mae_input.text().strip()
        pai = self.pai_input.text().strip()

        # Validação: todos os campos obrigatórios
        if not all([nome, identidade, nascimento, mae, pai]):
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        # Validação: nome não pode conter números
        if not nome.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Erro", "O nome deve conter apenas letras e espaços.")
            return

        try:
            # Conecta ao banco de dados
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            # Verifica duplicidade de nome (ignorando maiúsculas/minúsculas)
            cursor.execute("SELECT * FROM alunos WHERE LOWER(nome) = ?", (nome.lower(),))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Já existe um aluno com esse nome.")
                return

            # Insere o novo aluno no banco
            cursor.execute("""
                INSERT INTO alunos (nome, identidade, nascimento, nome_mae, nome_pai)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, identidade, nascimento, mae, pai))

            conn.commit()
            conn.close()

            # Cria objeto do tipo AlunoDetalhado
            aluno = AlunoDetalhado(nome, identidade, nascimento, mae, pai)

            # Atualiza a lista da janela principal, se houver callback
            if self.callback:
                self.callback(aluno)

            QMessageBox.information(self, "Sucesso", "Aluno cadastrado com sucesso!")
            self.close()  # Fecha a janela após cadastro bem-sucedido

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
