# Sistema Acadêmico

Este é um sistema acadêmico desenvolvido com **Python + PyQt5 + SQLite**, que permite gerenciar informações de alunos, disciplinas, notas e médias. A interface gráfica facilita o uso, sendo ideal para fins educacionais ou gestão acadêmica básica.

---

## ✅ Funcionalidades

- **Cadastro de Alunos**: Registre informações dos alunos no banco de dados.
- **Cadastro de Disciplinas**: Insira disciplinas que os alunos podem cursar.
- **Lançamento de Notas**: Associe notas aos alunos em cada disciplina.
- **Cálculo de Média**: Cálculo automático da média a partir das notas.
- **Visualização de Alunos, Disciplinas e Notas**: Interface amigável para listar todos os dados inseridos.

---

## 🧰 Tecnologias e Dependências

Este projeto depende de:

- `PyQt5==5.15.11` – Criação da interface gráfica
- `numpy==2.2.4` – Cálculo de médias
- `sqlite3` (nativo) – Banco de dados leve e embutido
- Outras dependências relacionadas ao uso com PyInstaller (para gerar executáveis)

Veja todas no `requirements.txt`.

---

## 💻 Instalação

### 1. Clone o repositório:
```bash
git clone https://github.com/HaurylanClaan/System_academic.git
```

### 2. Acesse a pasta do projeto:
```bash
cd sistema_academico
```

### 3. Crie e ative um ambiente virtual (recomendado):

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## ▶️ Como Usar

Para iniciar o sistema, execute o script principal:
```bash
python src/sistema_academico.py
```

A interface gráfica será exibida com as seguintes opções:

1. Cadastrar Disciplina
2. Ver Disciplinas Cadastradas
3. Cadastrar Aluno
4. Ver Alunos Cadastrados
5. Cadastrar Nota
6. Ver Notas por Aluno


---

## 🧭 Fluxo Sugerido de Uso

1. Cadastre os alunos
2. Cadastre as disciplinas
3. Lance as notas dos alunos
4. Visualize a média automaticamente calculada


---

## 📁 Estrutura do Projeto

```
sistema_academico/
├── docs/
│
├── src/                  # Código-fonte principal
│   ├── __init__.py
│   ├── aluno.py
│   ├── cadastro_aluno.py
│   ├── cadastro_disciplina.py
│   ├── cadastro_nota.py
│   ├── calculo_media.py
│   ├── calculos.py
│   ├── criar_banco.py
│   ├── database.py
│   ├── disciplina.py
│   ├── lancamento_notas.py
│   ├── lista_alunos.py
│   ├── lista_disciplinas.py
│   ├── sistema_academico.py
│   ├── ver_notas.py
│   └── sistema_academico.db
│
├── venv/                 # Ambiente virtual Python
├── requirements.txt      # Dependências do projeto
└── README.md
```


---

## 🙌 Contribuindo

1. Faça um fork
2. Crie uma branch: `git checkout -b minha-mudanca`
3. Faça commit: `git commit -m "minha melhoria"`
4. Push para o repositório: `git push origin minha-mudanca`
5. Abra um pull request

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
