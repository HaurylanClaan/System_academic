# Cadastro de disciplinas - integração com as outras pastas
# listas_disciplinas; disciplina.py; cadastro_disciplina
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from cadastro_disciplina import CadastroDisciplinaWindow
from lista_disciplinas import ListaDisciplinasWindow
from disciplina import Disciplina


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Acadêmico")
        self.setGeometry(100, 100, 600, 400)

        # Lista principal onde todas as disciplinas cadastradas são armazenadas
        self.disciplinas = []

        layout = QVBoxLayout()

        # Texto de boas-vindas
        self.label = QLabel("Bem-vindo ao Sistema Acadêmico", self)
        layout.addWidget(self.label)

        # Botão para cadastrar aluno (ainda será implementado)
        self.btn_cadastrar_aluno = QPushButton("Cadastrar Aluno", self)
        layout.addWidget(self.btn_cadastrar_aluno)

        # Botão para cadastrar disciplina
        self.btn_cadastrar_disciplina = QPushButton("Cadastrar Disciplina", self)
        self.btn_cadastrar_disciplina.clicked.connect(self.abrir_cadastro_disciplina)
        layout.addWidget(self.btn_cadastrar_disciplina)

        # Botão para ver disciplinas cadastradas
        self.btn_ver_disciplinas = QPushButton("Ver Disciplinas Cadastradas", self)
        self.btn_ver_disciplinas.clicked.connect(self.abrir_lista_disciplinas)
        layout.addWidget(self.btn_ver_disciplinas)

        # Botões ainda não implementados
        self.btn_lancar_notas = QPushButton("Lançar Notas", self)
        layout.addWidget(self.btn_lancar_notas)

        self.btn_calcular_media = QPushButton("Calcular Média", self)
        layout.addWidget(self.btn_calcular_media)

        self.setLayout(layout)

    # Abre a janela de cadastro de disciplina, passando a lista atual para verificação
    def abrir_cadastro_disciplina(self):
        self.janela_cadastro = CadastroDisciplinaWindow(self.adicionar_disciplina, self.disciplinas)
        self.janela_cadastro.show()

    # Adiciona nova disciplina à lista principal
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    # Abre a janela de listagem das disciplinas, com a função de remoção incluída
    def abrir_lista_disciplinas(self):
        self.janela_lista = ListaDisciplinasWindow(self.disciplinas, self.remover_disciplina)
        self.janela_lista.show()

    # Remove uma disciplina da lista
    def remover_disciplina(self, disciplina):
        self.disciplinas.remove(disciplina)


# Inicializa a aplicação
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
