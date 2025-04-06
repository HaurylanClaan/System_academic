from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema Acadêmico")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Bem-vindo ao Sistema Acadêmico", self)
        layout.addWidget(self.label)

        self.btn_cadastrar_aluno = QPushButton("Cadastrar Aluno", self)
        layout.addWidget(self.btn_cadastrar_aluno)

        self.btn_cadastrar_disciplina = QPushButton("Cadastrar Disciplina", self)
        layout.addWidget(self.btn_cadastrar_disciplina)

        self.btn_lancar_notas = QPushButton("Lançar Notas", self)
        layout.addWidget(self.btn_lancar_notas)

        self.btn_calcular_media = QPushButton("Calcular Média", self)
        layout.addWidget(self.btn_calcular_media)

        self.setLayout(layout)

# Inicializando a aplicação
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
