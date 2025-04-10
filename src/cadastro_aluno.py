from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sqlite3
from aluno import Aluno

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
            label = QLabel(texto)
            campo = QLineEdit()
            campo.setObjectName(chave)
            self.campos[chave] = campo
            layout.addWidget(label)
            layout.addWidget(campo)

        self.botao_salvar = QPushButton("Salvar")
        self.botao_salvar.clicked.connect(self.salvar_aluno)
        layout.addWidget(self.botao_salvar)

        self.setLayout(layout)

        # Atalhos com ENTER
        self.campos["nome"].returnPressed.connect(lambda: self.campos["identidade"].setFocus())
        self.campos["identidade"].returnPressed.connect(lambda: self.campos["nascimento"].setFocus())
        self.campos["nascimento"].returnPressed.connect(lambda: self.campos["nome_mae"].setFocus())
        self.campos["nome_mae"].returnPressed.connect(lambda: self.campos["nome_pai"].setFocus())
        self.campos["nome_pai"].returnPressed.connect(self.salvar_aluno)

    def salvar_aluno(self):
        dados = {k: self.campos[k].text().strip() for k in self.campos}
        if not all(dados.values()):
            QMessageBox.critical(self, "Erro", "Todos os campos são obrigatórios.")
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
            if "UNIQUE constraint failed: alunos.nome_normalizado" in str(e):
                QMessageBox.warning(self, "Erro", "Já existe um aluno com esse nome.")
            elif "UNIQUE constraint failed: alunos.identidade" in str(e):
                QMessageBox.warning(self, "Erro", "Já existe um aluno com essa identidade.")
            else:
                QMessageBox.critical(self, "Erro", f"Erro ao cadastrar: {e}")
