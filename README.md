# CP02_GRUPO3

# Prompt Toolkit — FIAP Checkpoint 02
Projeto desenvolvido para o Checkpoint 02 da disciplina de Prompt Engineering & Artificial Intelligence da FIAP.

O sistema consiste em um toolkit modular em Python capaz de aplicar automaticamente diferentes técnicas de prompting em tarefas de negócio utilizando modelos LLM executados localmente via Ollama.

# Integrantes
Gabriel Camarosani Gouvea Gonçalves da Silva RM: 569189

Gustavo Lima Andrade Santos RM: 571709

Lucas Seiji Hummel RM: 569673

Pedro Souza Castro RM: 569311

Bruno Yudi Moritaka Kanashiro RM: 571776

# Objetivo do Projeto

O objetivo do projeto é comparar técnicas de Prompt Engineering para identificar qual abordagem gera melhores resultados em tarefas de linguagem natural.

O toolkit executa automaticamente:

- Zero-Shot Prompting
- Few-Shot Prompting
- Chain of Thought (CoT)
- Role Prompting

Além disso, o sistema mede:

- Acurácia
- Quantidade de tokens
- Tempo de resposta
- Consistência

Ao final, o sistema gera:

- Tabela comparativa em CSV
- Gráficos automáticos
- Recomendação da melhor técnica

# Tecnologias Utilizadas

## Linguagem
- Python 3.10+

## Bibliotecas
- requests
- pandas
- matplotlib
- python-dotenv

## LLM
- Ollama API
- Modelo: gpt-oss:120b

# Instalação

## 1. Clonar e entrar na pasta
- git clone https://github.com/gabrielcggs/CP02_GRUPO3
- cd CP02_GRUPO3

## 2. Criar ambiente virtual
- python -m venv venv

## 3. Ative o ambiente virtual
Windows
- venv\Scripts\activate

Linux/Mac
- source venv/bin/activate

## 4. Instalar Dependências
- pip install -r requirements.txt

# Configurar Ollama
## Instalar Ollama
Site oficial: https://ollama.com/

## Baixar o modelo
ollama pull gpt-oss:120b

## Iniciar Ollama
ollama serve

# Executar Projeto
python main.py

# Técnicas Implementadas

## Zero-Shot 
Executa a tarefa sem exemplos.

Utiliza apenas:

- instrução
- contexto
- formato esperado

## Few-Shot
Executa a tarefa utilizando exemplos prévios.

Os exemplos são adicionados dinamicamente ao prompt.

## Chain of Thought (CoT)

Força o modelo a resolver a tarefa passo a passo.

Melhora:

- raciocínio
- coerência
- explicabilidade
















