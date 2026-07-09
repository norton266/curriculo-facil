# Currículo Fácil

Gerador de currículos em PDF desenvolvido com **Python**, **Flask** e **ReportLab**.

O objetivo do projeto é permitir que qualquer pessoa preencha um formulário simples e gere um currículo profissional em diferentes modelos, de forma rápida e gratuita.

---

# Funcionalidades

- Geração automática de currículo em PDF
- Upload de foto
- Múltiplos modelos de currículo
    - Moderno
    - Executivo
    - Minimalista
    - Duas Colunas
- Experiências dinâmicas
- Formações dinâmicas
- Certificações dinâmicas
- Habilidades dinâmicas
- Idiomas dinâmicos
- LinkedIn
- GitHub
- Salvamento automático do formulário (LocalStorage)
- Download imediato do PDF

---

# Tecnologias

## Backend

- Python 3
- Flask
- ReportLab

## Frontend

- HTML5
- CSS3
- JavaScript

---

# Estrutura do projeto

```
curriculo-facil/

├── app.py
│
├── models/
│
├── services/
│   ├── builders/
│   ├── componentes/
│   ├── layouts/
│   ├── modelos/
│   ├── parsers/
│   ├── pdf/
│   └── renderers/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── uploads/
│
└── pdfs/
```

---

# Arquitetura

O projeto foi organizado em camadas para manter baixo acoplamento e facilitar futuras expansões.

```
HTML
    ↓
Builders
    ↓
Models
    ↓
PDF Models
    ↓
Layouts
    ↓
Renderers
    ↓
ReportLab
```

Cada camada possui apenas uma responsabilidade.

---

# Builders

Os Builders são responsáveis por transformar os dados enviados pelo formulário em objetos do domínio.

Exemplo:

```
Request

↓

CurriculoBuilder

↓

Curriculo
```

---

# Layouts

Os layouts controlam apenas a organização visual do documento.

Atualmente existem:

- Layout de uma coluna
- Layout de duas colunas

Novos layouts podem ser adicionados sem alterar o restante do sistema.

---

# Renderers

Os Renderers encapsulam componentes específicos do ReportLab.

Isso permite alterar a biblioteca de geração de PDF futuramente com poucas modificações.

---

# Componentes

Os componentes representam partes reutilizáveis do currículo.

Exemplo:

- Cabeçalho
- Experiências
- Formação
- Sidebar
- Foto
- Contato
- Habilidades
- Idiomas

---

# Front-end

O formulário possui:

- Componentes separados
- JavaScript modularizado
- Templates reutilizáveis
- Adição dinâmica de campos
- Remoção dinâmica
- Salvamento automático no navegador

---

# Como executar

Clone o projeto

```bash
git clone https://github.com/seu-usuario/curriculo-facil.git
```

Entre na pasta

```bash
cd curriculo-facil
```

Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Linux

```bash
python3 -m venv .venv
```

Ative o ambiente

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute

```bash
python app.py
```

Acesse

```
http://localhost:5000
```

---

# Roadmap

## Back-end

- [x] Refatoração para Builders
- [x] Separação em Layouts
- [x] Separação em Renderers
- [x] PDF em memória (BytesIO)
- [ ] Testes unitários
- [ ] Exportação em DOCX
- [ ] API REST

## Front-end

- [x] Formulário modular
- [x] Campos dinâmicos
- [x] LocalStorage
- [ ] Preview em tempo real
- [ ] Drag and Drop de foto
- [ ] Tema escuro

---

# Contribuição

Contribuições são bem-vindas.

Caso tenha sugestões de melhorias, abra uma Issue ou envie um Pull Request.

---