from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3

class CadastroDisciplinaWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback  # Função para atualizar a lista na tela principal
        self.setWindowTitle("Cadastro de Disciplina")

        # Campos de entrada
        self.nome_input = QLineEdit()
        self.codigo_input = QLineEdit()

        # Botões
        self.salvar_btn = QPushButton("Salvar")
        self.cancelar_btn = QPushButton("Cancelar")

        # Conexões dos botões
        self.salvar_btn.clicked.connect(self.salvar_disciplina)
        self.cancelar_btn.clicked.connect(self.close)

        # Tecla Enter para usabilidade
        self.nome_input.returnPressed.connect(self.codigo_input.setFocus)
        self.codigo_input.returnPressed.connect(self.salvar_disciplina)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Nome da Disciplina:"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Código da Disciplina (apenas números):"))
        layout.addWidget(self.codigo_input)

        botoes = QHBoxLayout()
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(self.cancelar_btn)
        layout.addLayout(botoes)

        self.setLayout(layout)

    def salvar_disciplina(self):
        nome = self.nome_input.text().strip()
        codigo = self.codigo_input.text().strip()

        # Validação de campos obrigatórios
        if not nome or not codigo:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        # Validação do nome (apenas letras e espaços)
        if not nome.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Erro", "O nome deve conter apenas letras e espaços.")
            return

        # Validação do código (apenas números inteiros)
        if not codigo.isdigit():
            QMessageBox.warning(self, "Erro", "O código deve conter apenas números inteiros.")
            return

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            # Verificação de nome repetido (ignora maiúsculas/minúsculas)
            cursor.execute("SELECT * FROM disciplinas WHERE LOWER(nome) = ?", (nome.lower(),))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Já existe uma disciplina com esse nome.")
                return

            # Verificação de código repetido
            cursor.execute("SELECT * FROM disciplinas WHERE codigo = ?", (codigo,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Já existe uma disciplina com esse código.")
                return

            # Inserção no banco
            cursor.execute("""
                INSERT INTO disciplinas (nome, codigo)
                VALUES (?, ?)
            """, (nome, codigo))

            conn.commit()
            conn.close()

            # Callback para atualizar lista na MainWindow
            if self.callback:
                self.callback(nome)

            QMessageBox.information(self, "Sucesso", "Disciplina cadastrada com sucesso!")
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
    