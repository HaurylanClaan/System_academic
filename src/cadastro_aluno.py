from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from aluno import Aluno
import sqlite3

class CadastroAlunoWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.setWindowTitle("Cadastro de Aluno")
        self.callback = callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.campos = {}

        labels = {
            "nome": "Nome Completo",
            "identidade": "Número de Identidade",
            "nascimento": "Data de Nascimento",
            "nome_mae": "Nome da Mãe",
            "nome_pai": "Nome do Pai"
        }

        for chave, texto in labels.items():
            layout.addWidget(QLabel(texto))
            campo = QLineEdit()
            self.campos[chave] = campo
            layout.addWidget(campo)

        botao = QPushButton("Salvar")
        botao.clicked.connect(self.salvar)
        layout.addWidget(botao)

        self.setLayout(layout)

    def salvar(self):
        dados = {k: campo.text().strip() for k, campo in self.campos.items()}
        if not all(dados.values()):
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        aluno = Aluno(**dados)

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO alunos (nome, nome_normalizado, identidade, nascimento, nome_mae, nome_pai)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (aluno.nome, aluno.nome_normalizado, aluno.identidade, aluno.nascimento, aluno.nome_mae, aluno.nome_pai))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Sucesso", "Aluno cadastrado com sucesso!")
            if self.callback:
                self.callback(aluno)
            self.close()
        except sqlite3.IntegrityError as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar: {e}")
