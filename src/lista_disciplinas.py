# lista_disciplinas.py
# ---------------------
# Esta janela exibe a lista de disciplinas cadastradas.
# Permite pesquisar disciplinas por nome ou código, e também excluir uma disciplina selecionada.

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class ListaDisciplinasWindow(QWidget):
    def __init__(self, lista_disciplinas, remover_callback):
        super().__init__()
        self.setWindowTitle("Disciplinas Cadastradas")
        self.setGeometry(150, 150, 400, 300)

        # Lista de objetos Disciplina passados pela MainWindow
        self.lista_disciplinas = lista_disciplinas
        # Função de callback para remover uma disciplina (definida na MainWindow)
        self.remover_callback = remover_callback

        # Layout principal vertical
        layout = QVBoxLayout()

        # Campo de busca para filtrar disciplinas por nome ou código
        self.busca_input = QLineEdit(self)
        self.busca_input.setPlaceholderText("Pesquisar por nome ou código...")
        self.busca_input.textChanged.connect(self.atualizar_lista)
        layout.addWidget(self.busca_input)

        # Lista que mostra as disciplinas
        self.lista = QListWidget(self)
        layout.addWidget(self.lista)

        # Botão para excluir a disciplina selecionada
        self.btn_excluir = QPushButton("Excluir Disciplina Selecionada", self)
        self.btn_excluir.clicked.connect(self.excluir_disciplina)
        layout.addWidget(self.btn_excluir)

        # Define o layout e preenche a lista inicialmente
        self.setLayout(layout)
        self.atualizar_lista()

    def atualizar_lista(self):
        """Atualiza a lista com base no termo digitado no campo de busca."""
        termo = self.busca_input.text().lower()
        self.lista.clear()

        # Adiciona à lista apenas as disciplinas que contêm o termo no nome ou no código
        for d in self.lista_disciplinas:
            if termo in d.nome.lower() or termo in d.codigo.lower():
                self.lista.addItem(str(d))

    def excluir_disciplina(self):
        """Remove a disciplina selecionada após confirmação do usuário."""
        item_selecionado = self.lista.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Atenção", "Selecione uma disciplina para excluir.")
            return

        nome_completo = item_selecionado.text()

        # Procura a disciplina correspondente e solicita confirmação antes de excluir
        for d in self.lista_disciplinas:
            if str(d) == nome_completo:
                confirmacao = QMessageBox.question(
                    self,
                    "Confirmar Exclusão",
                    f"Tem certeza que deseja excluir a disciplina:\n\n{d}?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if confirmacao == QMessageBox.Yes:
                    self.remover_callback(d)  # Chama a função de remoção da MainWindow
                    self.atualizar_lista()   # Atualiza a lista após remoção
                return
