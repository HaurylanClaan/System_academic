from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sqlite3

class LancamentoNotasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lançamento de Notas")

        # Campos de entrada
        self.id_aluno_input = QLineEdit()
        self.id_disciplina_input = QLineEdit()
        self.nota_input = QLineEdit()

        # Botões
        self.salvar_btn = QPushButton("Salvar Nota")
        self.cancelar_btn = QPushButton("Cancelar")

        # Conexões
        self.salvar_btn.clicked.connect(self.lancar_nota)
        self.cancelar_btn.clicked.connect(self.close)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("ID do Aluno:"))
        layout.addWidget(self.id_aluno_input)
        layout.addWidget(QLabel("ID da Disciplina:"))
        layout.addWidget(self.id_disciplina_input)
        layout.addWidget(QLabel("Nota (0 a 10):"))
        layout.addWidget(self.nota_input)

        botoes = QHBoxLayout()
        botoes.addWidget(self.salvar_btn)
        botoes.addWidget(self.cancelar_btn)
        layout.addLayout(botoes)

        self.setLayout(layout)

    def lancar_nota(self):
        aluno_id = self.id_aluno_input.text().strip()
        disciplina_id = self.id_disciplina_input.text().strip()
        nota = self.nota_input.text().strip()

        # Verificações básicas
        if not aluno_id or not disciplina_id or not nota:
            QMessageBox.warning(self, "Erro", "Todos os campos são obrigatórios.")
            return

        if not aluno_id.isdigit() or not disciplina_id.isdigit():
            QMessageBox.warning(self, "Erro", "ID do aluno e da disciplina devem ser números.")
            return

        try:
            nota_valor = float(nota)
            if nota_valor < 0 or nota_valor > 10:
                QMessageBox.warning(self, "Erro", "A nota deve estar entre 0 e 10.")
                return
        except ValueError:
            QMessageBox.warning(self, "Erro", "Nota inválida. Use ponto como separador decimal.")
            return

        try:
            conn = sqlite3.connect("sistema_academico.db")
            cursor = conn.cursor()

            # Verifica se aluno existe
            cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
            if not cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Aluno não encontrado.")
                return

            # Verifica se disciplina existe
            cursor.execute("SELECT * FROM disciplinas WHERE id = ?", (disciplina_id,))
            if not cursor.fetchone():
                QMessageBox.warning(self, "Erro", "Disciplina não encontrada.")
                return

            # Tenta atualizar se a nota já existir (garantindo que não haja duplicidade)
            cursor.execute("""
                SELECT * FROM notas
                WHERE aluno_id = ? AND disciplina_id = ?
            """, (aluno_id, disciplina_id))
            if cursor.fetchone():
                cursor.execute("""
                    UPDATE notas
                    SET nota = ?
                    WHERE aluno_id = ? AND disciplina_id = ?
                """, (nota_valor, aluno_id, disciplina_id))
                conn.commit()
                QMessageBox.information(self, "Atualizado", "Nota atualizada com sucesso.")
            else:
                cursor.execute("""
                    INSERT INTO notas (aluno_id, disciplina_id, nota)
                    VALUES (?, ?, ?)
                """, (aluno_id, disciplina_id, nota_valor))
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Nota lançada com sucesso.")

            conn.close()
            self.close()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", str(e))
