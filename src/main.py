from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from cadastro_disciplina import CadastroDisciplinaWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Acadêmico")
        self.setGeometry(100, 100, 400, 300)

        self.botao_cadastrar = QPushButton("Cadastrar Disciplina")
        self.botao_cadastrar.clicked.connect(self.abrir_cadastro_disciplina)

        layout = QVBoxLayout()
        layout.addWidget(self.botao_cadastrar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_cadastro_disciplina(self):
        self.janela_cadastro = CadastroDisciplinaWindow(callback=self.atualizar_lista_disciplinas)
        self.janela_cadastro.show()

    def atualizar_lista_disciplinas(self, nome):
        print(f"Disciplina '{nome}' cadastrada!")  # Aqui você pode atualizar alguma lista/GUI
