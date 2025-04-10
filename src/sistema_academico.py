from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from cadastro_aluno import CadastroAlunoWindow
from cadastro_disciplina import CadastroDisciplinaWindow
from lista_disciplinas import ListaDisciplinasWindow
from database import carregar_disciplinas, inicializar_banco
from lista_alunos import ListaAlunosWindow
from database import carregar_alunos
from cadastro_nota import CadastroNotaWindow
from ver_notas import VerNotasWindow


class MainWindow(QWidget):
    from ver_notas import VerNotasWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Acadêmico")
        self.setGeometry(100, 100, 600, 400)

        self.disciplinas = carregar_disciplinas()  # ← Carrega do banco

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bem-vindo ao Sistema Acadêmico"))

        # Botão para cadastrar disciplina
        btn_cadastrar_disciplina = QPushButton("Cadastrar Disciplina")
        btn_cadastrar_disciplina.clicked.connect(self.abrir_cadastro_disciplina)
        layout.addWidget(btn_cadastrar_disciplina)

        # Botão para listar disciplinas
        btn_listar = QPushButton("Ver Disciplinas Cadastradas")
        btn_listar.clicked.connect(self.abrir_lista_disciplinas)
        layout.addWidget(btn_listar)

        # Botão para cadastrar aluno
        btn_cadastrar_aluno = QPushButton("Cadastrar Aluno")
        btn_cadastrar_aluno.clicked.connect(self.abrir_cadastro_aluno)
        layout.addWidget(btn_cadastrar_aluno)

        btn_listar_alunos = QPushButton("Ver Alunos Cadastrados")
        btn_listar_alunos.clicked.connect(self.abrir_lista_alunos)
        layout.addWidget(btn_listar_alunos)
        self.setLayout(layout)

        btn_cadastrar_nota = QPushButton("Cadastrar Nota")
        btn_cadastrar_nota.clicked.connect(self.abrir_cadastro_nota)
        layout.addWidget(btn_cadastrar_nota)

        # Botão para ver notas por aluno
        btn_ver_notas = QPushButton("Ver Notas por Aluno")
        btn_ver_notas.clicked.connect(self.abrir_ver_notas)
        layout.addWidget(btn_ver_notas)


    def abrir_cadastro_disciplina(self):
        self.janela_cadastro = CadastroDisciplinaWindow(callback=self.adicionar_disciplina)
        self.janela_cadastro.show()

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def abrir_lista_disciplinas(self):
        self.janela_lista = ListaDisciplinasWindow(self.disciplinas, self.remover_disciplina)
        self.janela_lista.show()

    def remover_disciplina(self, disciplina):
        self.disciplinas.remove(disciplina)

    def abrir_cadastro_aluno(self):
        self.janela_aluno = CadastroAlunoWindow()
        self.janela_aluno.show()

    def abrir_lista_alunos(self):
        alunos = carregar_alunos()
        self.janela_lista_alunos = ListaAlunosWindow(alunos)
        self.janela_lista_alunos.show()

    def abrir_cadastro_nota(self):
        self.janela_nota = CadastroNotaWindow()
        self.janela_nota.show()
    def abrir_ver_notas(self):
        self.janela_ver_notas = VerNotasWindow()
        self.janela_ver_notas.show()


# Ponto de entrada
if __name__ == "__main__":
    inicializar_banco()
    app = QApplication([])
    # Estilo global
    style = """
        QWidget {
            background-color: #f8f9fa;
            font-family: Arial;
            font-size: 14px;
        }

        QPushButton {
            background-color: #007bff;
            color: white;
            padding: 8px;
            border-radius: 5px;
        }

        QPushButton:hover {
            background-color: #0056b3;
        }

        QLabel {
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        QLineEdit, QComboBox {
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
    """
    app.setStyleSheet(style)
    window = MainWindow()
    window.show()
    app.exec_()
