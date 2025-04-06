# Sistema Acadêmico

Este é um sistema acadêmico para gerenciar e calcular informações relacionadas a alunos e disciplinas. Ele permite realizar o cadastro de alunos, lançamento de notas, cadastro de disciplinas e cálculo da média dos alunos.

## Funcionalidades

- **Cadastro de Alunos**: Registre informações dos alunos no sistema.
- **Lançamento de Notas**: Adicione e atualize as notas dos alunos em suas respectivas disciplinas.
- **Cadastro de Disciplinas**: Adicione novas disciplinas ao sistema.
- **Cálculo de Média**: Calcule a média das notas dos alunos nas disciplinas cadastradas.

## Bibliotecas e Dependências

Este projeto utiliza várias bibliotecas Python para garantir a funcionalidade do sistema. As dependências incluem:

- **altgraph==0.17.4**: Usado para análise de gráficos de dependência.
- **numpy==2.2.4**: Biblioteca para computação numérica (usada no cálculo de médias).
- **packaging==24.2**: Para a manipulação de pacotes.
- **pefile==2023.2.7**: Para análise de arquivos PE (Portable Executable).
- **pyinstaller==6.12.0**: Para gerar executáveis do Python.
- **pyinstaller-hooks-contrib==2025.2**: Hooks para bibliotecas utilizadas com PyInstaller.
- **PyQt5==5.15.11**: Biblioteca gráfica para criar interfaces de usuário (UI).
- **PyQt5-Qt5==5.15.2**: Qt5 bindings para PyQt5.
- **PyQt5_sip==12.17.0**: Interface de binding de Python para o Qt.
- **pywin32-ctypes==0.2.3**: Funcionalidades específicas para Windows.
- **setuptools==78.1.0**: Usado para empacotar e distribuir pacotes Python.

## Instalação

1. **Clone este repositório** para sua máquina local:

   ```bash
   git clone https://github.com/HaurylanClaan/sistema_academico.git

## Entrar na pasta do projeto:

```bash
cd pasta_onde_o_projetofoibaixado
```

## Criar e ativar um ambiente virtual (opcional, mas recomendado):

### No Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## Como Usar

### Executar o Sistema e iniciar a interface gráfica:
Após a instalação das dependências, você pode iniciar o sistema acadêmico executando o script principal do projeto `sistema_academico.py`.


---

## Funcionalidades

- **Cadastrar Alunos**: No menu de cadastro de alunos, insira os dados solicitados, como nome, matrícula e dados adicionais.
- **Cadastrar Disciplinas**: Registre as disciplinas que os alunos cursam e associe-as aos respectivos alunos.
- **Lançamento de Notas**: Insira as notas dos alunos nas disciplinas correspondentes e visualize os resultados.
- **Cálculo de Média**: O sistema calculará automaticamente a média dos alunos com base nas notas lançadas.

---

## Exemplo de Execução

Ao executar o script, você verá uma interface gráfica onde poderá interagir com o sistema. O fluxo básico é:

1. Cadastro de Alunos  
2. Cadastro de Disciplinas  
3. Lançamento de Notas  
4. Cálculo de Média  

---

## 📁 Estrutura do Projeto

```
PROJETO_SISTEMA_ACADEMICO/
│
├── 📁 ambiente_virtual/           # Ambiente virtual Python (venv)
│   ├── 📁 Include/
│   ├── 📁 Lib/
│   ├── 📁 Scripts/
│   └── 📄 pyvenv.cfg
│
├── 📁 docs/                       # Documentação do projeto
│   └── 📁 src/
│       ├── 📄 index.html
│       ├── 📄 search.js
│       └── 📄 src.html
│
├── 📁 src/                        # Código-fonte principal do sistema
│   ├── 📁 __pycache__/            # Arquivos cache do Python
│   ├── 📄 __init__.py             # Inicializa o pacote Python
│   ├── 📄 aluno.py                # Cadastro e manipulação de alunos
│   ├── 📄 calculos.py             # Cálculos diversos (ex: médias)
│   ├── 📄 disciplina.py           # Cadastro de disciplinas
│   ├── 📄 lancamento_notas.py     # Lançamento de notas
│   └── 📄 sistema_academico.py    # Arquivo principal do sistema
│
├── 📄 requirements.txt            # Lista de dependências do projeto
└── 📄 .gitignore                  # Arquivos/pastas ignorados pelo Git
```



## Contribuindo

Se você gostaria de contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.  
2. Crie uma nova branch:
   ```bash
   git checkout -b feature/novidade
   ```
3. Faça suas alterações e commit.
4. Envie suas mudanças para o repositório remoto:
   ```bash
   git push origin feature/novidade
   ```
5. Abra um pull request.

---

## Licença
Este projeto está licenciado sob os termos da [MIT License](./LICENSE).
veja o arquivo LICENSE para mais detalhes.
