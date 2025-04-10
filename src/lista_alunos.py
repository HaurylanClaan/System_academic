# lista_alunos.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QMessageBox
from database import excluir_aluno, carregar_alunos

class ListaAlunosWindow(QWidget):
    def __init__(self, alunos_callback=None):
        super().__init__()
        self.setWindowTitle("Alunos Cadastrados")
        self.setGeometry(150, 150, 500, 400)

        self.alunos_callback = alunos_callback

        self.layout = QVBoxLayout()
        self.lista = QListWidget()

        self.layout.addWidget(QLabel("Lista de Alunos:"))
        self.layout.addWidget(self.lista)

        self.botao_excluir = QPushButton("Excluir Selecionado")
        self.botao_excluir.clicked.connect(self.excluir_selecionado)
        self.layout.addWidget(self.botao_excluir)

        self.setLayout(self.layout)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.clear()
        self.alunos = carregar_alunos()

        for aluno in self.alunos:
            nome, identidade, nascimento, nome_mae, nome_pai = aluno
            texto = f"{nome} | {identidade} | {nascimento} | {nome_mae} | {nome_pai}"
            item = QListWidgetItem(texto)
            item.setData(1000, identidade)  # Armazena identidade como dado interno
            self.lista.addItem(item)

    def excluir_selecionado(self):
        item = self.lista.currentItem()
        if not item:
            QMessageBox.warning(self, "Atenção", "Selecione um aluno para excluir.")
            return

        identidade = item.data(1000)
        nome = item.text().split("|")[0].strip()

        confirm = QMessageBox.question(
            self, "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o aluno:\n\n{nome}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            excluir_aluno(identidade)
            QMessageBox.information(self, "Sucesso", f"Aluno '{nome}' excluído com sucesso.")
            self.atualizar_lista()
