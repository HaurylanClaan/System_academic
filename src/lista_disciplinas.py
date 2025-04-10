# lista_disciplinas.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListWidget, QPushButton, QMessageBox
from database import excluir_disciplina

class ListaDisciplinasWindow(QWidget):
    def __init__(self, lista_disciplinas, remover_callback):
        super().__init__()
        self.setWindowTitle("Disciplinas Cadastradas")
        self.setGeometry(150, 150, 400, 300)

        self.lista_disciplinas = lista_disciplinas
        self.remover_callback = remover_callback

        layout = QVBoxLayout()

        self.busca_input = QLineEdit()
        self.busca_input.setPlaceholderText("Pesquisar por nome ou código...")
        self.busca_input.textChanged.connect(self.atualizar_lista)
        layout.addWidget(self.busca_input)

        self.lista = QListWidget()
        layout.addWidget(self.lista)

        self.btn_excluir = QPushButton("Excluir Disciplina Selecionada")
        self.btn_excluir.clicked.connect(self.excluir_disciplina)
        layout.addWidget(self.btn_excluir)

        self.setLayout(layout)
        self.atualizar_lista()

    def atualizar_lista(self):
        termo = self.busca_input.text().lower()
        self.lista.clear()

        for nome, codigo in self.lista_disciplinas:
            if termo in nome.lower() or termo in codigo.lower():
                self.lista.addItem(f"{nome} ({codigo})")

    def excluir_disciplina(self):
        item = self.lista.currentItem()
        if not item:
            QMessageBox.warning(self, "Aviso", "Selecione uma disciplina para excluir.")
            return

        texto = item.text()
        nome = texto.split(" (")[0]
        codigo = texto.split("(")[-1].replace(")", "")

        confirmacao = QMessageBox.question(
            self,
            "Confirmar Exclusão",
            f"Deseja excluir a disciplina:\n\n{nome} ({codigo})?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacao == QMessageBox.Yes:
            excluir_disciplina(nome, codigo)
            self.remover_callback((nome, codigo))
            self.atualizar_lista()
