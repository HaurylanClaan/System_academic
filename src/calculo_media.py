from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sqlite3

class CalculoMediaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cálculo de Média")

        # Campos de entrada
        self.id_aluno_input = QLineEdit()
        self.id_disciplina_input = QLineEdit()

        # Botão
        self.calcular_btn = QPushButton("Calcular Média")
        self.calcular_btn.clicked.connect(self.calcular_media)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("ID do Aluno (opcional):"))
        layout.addWidget(self.id_aluno_input)
        layout.addWidget(QLabel("ID da Disciplina (opcional):"))
        layout.addWidget(self.id_disciplina_input)
        layout.addWidget(self.calcular_btn)

        self.setLayout(layout)

    def calcular_media(self):
        aluno_id = self.id_aluno_input.text().strip()
        disciplina_id = self.id_disciplina_input.text().strip()

        query = "SELECT ROUND(AVG(nota), 2) FROM notas WHERE 1=1"
        params = []

        # Aplica filtros conforme necessário
        if aluno_id:
            if not aluno_id.isdigit():
                QMessageBox.warning(self, "Erro", "ID do aluno deve ser um número.")
                return
            query += " AND aluno_id = ?"
            params.append(aluno_id)

        if disciplina_id:
            if not disciplina_id.isdigit():
                QMessageBox.warning(self, "Erro", "ID da disciplina deve ser um número.")
                return
            query += " AND disciplina_id = ?"
            params.append(disciplina_id)

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            cursor.execute(query, params)
            resultado = cursor.fetchone()
            media = resultado[0]

            if media is not None:
                QMessageBox.information(self, "Média Calculada", f"A média é: {media}")
            else:
                QMessageBox.information(self, "Sem Dados", "Nenhuma nota encontrada para o(s) filtro(s) informado(s).")

            conn.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
