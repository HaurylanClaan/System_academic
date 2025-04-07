# cadastro_disciplina.py
# -----------------------
# Janela para cadastrar uma nova disciplina no sistema.
# Valida o nome (apenas letras e acentos) e o código (apenas números inteiros),
# além de verificar se já existe uma disciplina com o mesmo nome ou código.

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from disciplina import Disciplina
import re  # Usado para validação com expressões regulares

class CadastroDisciplinaWindow(QWidget):
    def __init__(self, adicionar_callback, disciplinas_existentes):
        super().__init__()
        self.setWindowTitle("Cadastrar Disciplina")
        self.setGeometry(150, 150, 300, 200)

        # Callback usado para adicionar uma nova disciplina à lista principal
        self.adicionar_callback = adicionar_callback
        self.disciplinas_existentes = disciplinas_existentes  # Lista de disciplinas já cadastradas

        layout = QVBoxLayout()

        # Campo de entrada para o nome da disciplina
        self.input_nome = QLineEdit(self)
        self.input_nome.setPlaceholderText("Nome da Disciplina")
        self.input_nome.returnPressed.connect(self.foco_para_codigo)  # Pressionar Enter vai para o campo de código
        layout.addWidget(self.input_nome)

        # Campo de entrada para o código da disciplina
        self.input_codigo = QLineEdit(self)
        self.input_codigo.setPlaceholderText("Código da Disciplina")
        self.input_codigo.returnPressed.connect(self.salvar_disciplina)  # Pressionar Enter aciona o salvamento
        layout.addWidget(self.input_codigo)

        # Botão para salvar a disciplina
        self.btn_salvar = QPushButton("Salvar", self)
        self.btn_salvar.clicked.connect(self.salvar_disciplina)
        layout.addWidget(self.btn_salvar)

        self.setLayout(layout)

    # Define o foco no campo de código quando o usuário aperta Enter no campo nome
    def foco_para_codigo(self):
        self.input_codigo.setFocus()

    # Função chamada ao salvar a disciplina
    def salvar_disciplina(self):
        nome = self.input_nome.text().strip()
        codigo = self.input_codigo.text().strip()

        # Verifica se todos os campos foram preenchidos
        if not nome or not codigo:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        # Valida o nome: apenas letras e acentos (com espaços)
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            QMessageBox.warning(self, "Erro", "O nome deve conter apenas letras e acentos!")
            return

        # Valida se o código é composto apenas por números inteiros
        if not codigo.isdigit():
            QMessageBox.warning(self, "Erro", "O código deve conter apenas números inteiros!")
            return

        # Verifica se já existe disciplina com mesmo nome ou mesmo código
        for d in self.disciplinas_existentes:
            if d.nome.lower() == nome.lower():
                QMessageBox.warning(self, "Erro", f"A disciplina '{nome}' já está cadastrada!")
                return
            if d.codigo == codigo:
                QMessageBox.warning(self, "Erro", f"O código '{codigo}' já está em uso por outra disciplina!")
                return

        # Cria nova disciplina e adiciona via callback
        nova = Disciplina(nome, codigo)
        self.adicionar_callback(nova)

        # Informa sucesso e fecha a janela
        QMessageBox.information(self, "Sucesso", "Disciplina cadastrada com sucesso!")
        self.close()
