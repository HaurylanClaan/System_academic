# cadastro_nota.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit, QMessageBox
from database import conectar, salvar_nota

class CadastroNotaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Notas")
        self.setGeometry(200, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Alunos
        layout.addWidget(QLabel("Selecione o Aluno:"))
        self.combo_alunos = QComboBox()
        self.carregar_alunos()
        layout.addWidget(self.combo_alunos)

        # Disciplinas
        layout.addWidget(QLabel("Selecione a Disciplina:"))
        self.combo_disciplinas = QComboBox()
        self.carregar_disciplinas()
        layout.addWidget(self.combo_disciplinas)

        # Notas
        layout.addWidget(QLabel("Nota 1:"))
        self.input_nota1 = QLineEdit()
        layout.addWidget(self.input_nota1)

        layout.addWidget(QLabel("Nota 2:"))
        self.input_nota2 = QLineEdit()
        layout.addWidget(self.input_nota2)

        # Botão salvar
        btn_salvar = QPushButton("Salvar Nota")
        btn_salvar.clicked.connect(self.salvar)
        layout.addWidget(btn_salvar)

        self.setLayout(layout)

    def carregar_alunos(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM alunos")
        self.alunos = cursor.fetchall()
        conn.close()
        self.combo_alunos.clear()
        for id_, nome in self.alunos:
            self.combo_alunos.addItem(nome, id_)

    def carregar_disciplinas(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome FROM disciplinas")
        self.disciplinas = cursor.fetchall()
        conn.close()
        self.combo_disciplinas.clear()
        for id_, nome in self.disciplinas:
            self.combo_disciplinas.addItem(nome, id_)

    def salvar(self):
        try:
            aluno_id = self.combo_alunos.currentData()
            disciplina_id = self.combo_disciplinas.currentData()
            nota1 = float(self.input_nota1.text().strip())
            nota2 = float(self.input_nota2.text().strip())

            salvar_nota(aluno_id, disciplina_id, nota1, nota2)

            QMessageBox.information(self, "Sucesso", "Nota salva com sucesso!")
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos para as notas.")
