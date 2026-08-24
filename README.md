# Currículo Fácil

> Gere currículos profissionais em PDF em poucos minutos.

Projeto desenvolvido com foco em arquitetura de software, organização de código e boas práticas de desenvolvimento em Python.

Além de gerar currículos em diferentes modelos, o projeto utiliza uma arquitetura modular baseada em Builders, Layouts, Renderers, componentes reutilizáveis e separação de responsabilidades (SRP).

Atualmente, o projeto também está evoluindo para incorporar **Inteligência Artificial através de uma LLM (Large Language Model)**, permitindo que o usuário possa futuramente criar seu currículo através de uma conversa natural com o sistema.

A proposta é auxiliar principalmente pessoas que possuem dificuldade de escrita, organização de informações ou pouca familiaridade com ferramentas digitais.

---

# Funcionalidades

## Geração de currículo

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

## Inteligência Artificial

O projeto possui uma integração com uma **LLM (Large Language Model)** utilizando a **Gemini API**.

A proposta da Inteligência Artificial é permitir que o usuário construa seu currículo através de uma conversa natural, sem precisar conhecer previamente a estrutura de um currículo ou saber exatamente como descrever suas experiências.

Por exemplo:

```text
IA:
Olá! Vou te ajudar a criar seu currículo.
Qual é o seu nome?

Usuário:
João da Silva

IA:
Ótimo, João! Você possui experiência profissional?

Usuário:
Sim, trabalhei dois anos em uma loja como vendedor.

IA:
Legal! Qual era o nome da empresa e quais eram suas principais atividades?

Usuário:
Loja X. Eu atendia clientes, organizava produtos
e também cuidava do caixa.

---
```
A partir da conversa, a aplicação deverá identificar e organizar as informações relevantes para a construção do currículo.

Estado atual da Inteligência Artificial

A integração inicial com a Gemini API já foi implementada.

Implementado
 Integração com Gemini API
 Configuração da API através de .env
 Criação do LLMService
 Envio de mensagens para a LLM
 Recebimento de respostas da Gemini
 Teste inicial de comunicação com a LLM
 Primeira resposta funcional da IA

Em desenvolvimento
 Implementação completa do CurriculoAI
 Definição do fluxo de entrevista
 Memória/contexto da conversa
 Prompt especializado para criação de currículos
 Extração estruturada das informações
 Validação das informações coletadas
 Confirmação dos dados pelo usuário
 Integração com o modelo Curriculo
 Integração com o CurriculoBuilder
 Geração automática do currículo a partir da conversa
 Interface de chat no frontend

Atualmente, a LLM já consegue receber uma mensagem e gerar uma resposta, porém o fluxo completo de criação do currículo através da conversa ainda está em desenvolvimento.

Objetivo da Inteligência Artificial

A IA será responsável por conduzir uma entrevista conversacional com o usuário.

O objetivo é transformar informações fornecidas de maneira livre e desestruturada em informações organizadas que possam ser utilizadas pelo sistema de geração de currículos.

o fluxo planejado é:

Usuário inicia a conversa
        ↓
IA identifica o objetivo profissional
        ↓
IA coleta dados pessoais
        ↓
IA coleta experiências profissionais
        ↓
IA coleta formação acadêmica
        ↓
IA coleta cursos e certificações
        ↓
IA identifica habilidades
        ↓
IA identifica idiomas
        ↓
IA solicita informações adicionais
        ↓
IA apresenta um resumo
        ↓
Usuário confirma ou corrige
        ↓
Dados estruturados
        ↓
CurriculoBuilder
        ↓
Geração do PDF

Arquitetura da Inteligência Artificial

A integração da LLM foi desenvolvida de forma separada do restante da aplicação, mantendo baixo acoplamento entre o provedor de IA e as regras de negócio do sistema.

Arquitetura atual:

Usuário
    ↓
CurriculoAI
    ↓
LLMService
    ↓
Gemini API
    ↓
Resposta da IA

Arquitetura planejada:

                    Usuário
                       ↓
              Interface de Chat
                       ↓
                  CurriculoAI
                       ↓
          ┌────────────┴────────────┐
          ↓                         ↓
 Estado da conversa              Prompt
          │                         │
          └────────────┬────────────┘
                       ↓
                  LLMService
                       ↓
                  Gemini API
                       ↓
                Resposta da IA
                       ↓
            Informações estruturadas
                       ↓
                   Curriculo
                       ↓
                CurriculoBuilder
                       ↓
                    Layout
                       ↓
                   Renderer
                       ↓
                   ReportLab
                       ↓
                      PDF

Essa separação permite que o provedor da LLM possa ser alterado futuramente sem modificar as regras principais da aplicação.

Estrutura de dados planejada

A conversa com a IA não deverá resultar apenas em um texto livre.

A aplicação deverá transformar as informações coletadas em dados estruturados.

Exemplo:

{
    "dados_pessoais": {
        "nome": "João da Silva",
        "email": "joao@email.com",
        "telefone": "51999999999"
    },
    "objetivo": "Auxiliar Administrativo",
    "experiencias": [
        {
            "empresa": "Empresa X",
            "cargo": "Auxiliar Administrativo",
            "periodo": "2024 - 2026",
            "descricao": "Atendimento ao cliente, organização de documentos e controle de planilhas."
        }
    ],
    "formacao": [],
    "certificacoes": [],
    "habilidades": [
        "Excel",
        "Atendimento ao cliente",
        "Organização"
    ],
    "idiomas": []
}

Esses dados poderão ser utilizados pelo modelo de domínio existente:

Conversa
    ↓
LLM
    ↓
Dados estruturados
    ↓
Curriculo
    ↓
CurriculoBuilder
    ↓
Layouts
    ↓
Renderers
    ↓
ReportLab
    ↓
PDF

Funcionalidades planejadas para a IA

Além da criação do currículo através de uma conversa, a LLM poderá futuramente ser utilizada para:

Criar currículo a partir de informações desestruturadas
Auxiliar usuários com dificuldade de escrita
Melhorar descrições de experiências profissionais
Sugerir formas mais profissionais de apresentar experiências
Identificar habilidades a partir das experiências informadas
Adaptar o currículo para uma vaga específica
Identificar informações que estão faltando
Sugerir melhorias no currículo
Auxiliar na criação do objetivo profissional
Gerar descrições profissionais sem inventar experiências
Solicitar confirmação antes de alterar informações importantes

Tecnologias

Backend

Python 3
Flask
ReportLab
Google Gemini API
Google GenAI SDK
python-dotenv

Frontend

HTML5
CSS3
JavaScript
LocalStorage
Inteligência Artificial
LLM (Large Language Model)
Gemini API
google-genai

Testes

pytest
