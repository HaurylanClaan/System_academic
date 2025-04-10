from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import re
import sqlite3
from database import salvar_disciplina

class CadastroDisciplinaWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback

        self.setWindowTitle("Cadastro de Disciplina")

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Nome da Disciplina")

        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText("Código da Disciplina")

        self.salvar_btn = QPushButton("Salvar")
        self.salvar_btn.clicked.connect(self.salvar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Código:"))
        layout.addWidget(self.codigo_input)
        layout.addWidget(self.salvar_btn)
        self.setLayout(layout)

    def salvar(self):
        nome = self.nome_input.text().strip()
        codigo = self.codigo_input.text().strip()

        if not nome or not codigo:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        # Validação opcional
        if not re.match(r'^[A-Za-z0-9]+$', codigo):
            QMessageBox.warning(self, "Erro", "Código inválido. Use apenas letras e números.")
            return

        # Tenta salvar no banco e trata erro de duplicação
        try:
            salvar_disciplina(nome, codigo)
            QMessageBox.information(self, "Sucesso", "Disciplina cadastrada com sucesso!")

            if self.callback:
                self.callback((nome, codigo))  # Retorna a tupla
            self.close()

        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Erro", f"O código '{codigo}' já está cadastrado. Use outro.")
