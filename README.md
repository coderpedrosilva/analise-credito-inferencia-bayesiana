# 📊 Análise de Crédito com Aprendizagem Bayesiana

## 📌 Visão Geral
Este projeto tem como objetivo aplicar conceitos de Aprendizagem Bayesiana para análise de risco de crédito, utilizando dados sintéticos e estatística probabilística em Python.

O foco do projeto é demonstrar, de forma prática e didática, como a probabilidade condicional pode auxiliar na tomada de decisão em cenários reais, como a identificação de clientes com maior risco de inadimplência.

Este é um projeto de nível júnior, voltado para estudos iniciais em Ciência de Dados, Estatística e Machine Learning.

---

## 🧠 Conceito: Aprendizagem Bayesiana
A Aprendizagem Bayesiana é baseada no Teorema de Bayes, que permite atualizar probabilidades à medida que novas evidências são observadas.

De forma simplificada, o projeto responde à seguinte pergunta:

> Qual é a probabilidade de um cliente ser inadimplente dado que ele já atrasou um pagamento?

Essa abordagem é amplamente utilizada em:
- Análise de risco de crédito
- Sistemas de apoio à decisão
- Modelos probabilísticos

---

## 📁 Arquitetura do Projeto

```text
aprendizagem_bayesiana/
│
├── data/
│ ├── credito.csv # Base de dados sintética
│ └── gerar_dados.py # Script de geração dos dados
│
├── src/
│ ├── carregar_dados.py # Leitura da base de dados
│ ├── tratamento.py # Limpeza e tratamento dos dados
│ ├── analise_exploratoria.py # Análise exploratória e gráficos
│ └── bayes.py # Cálculo Bayesiano
│
├── img/ # Imagens geradas pelos gráficos
├── main.py # Arquivo principal do projeto
└── README.md
```

---

## 📄 Descrição dos Arquivos

### data/gerar_dados.py
Responsável por gerar uma base de dados sintética de crédito, contendo informações como idade, renda, score de crédito, atraso em pagamento e inadimplência.

O script também insere dados inconsistentes propositalmente, permitindo demonstrar técnicas de tratamento de dados.

---

### data/credito.csv
Base de dados utilizada no projeto.

Os dados simulam um cenário real de análise de crédito e são usados em todas as etapas de análise e modelagem.

---

### src/carregar_dados.py
Arquivo responsável pela leitura do arquivo CSV e carregamento dos dados em um DataFrame pandas.

---

### src/tratamento.py
Contém as funções de limpeza e tratamento dos dados, como:
- Correção de valores negativos
- Ajuste de idades irreais
- Correção de scores fora do intervalo válido

---

### src/analise_exploratoria.py
Responsável pela análise exploratória dos dados (EDA) e geração dos gráficos.

Essa etapa ajuda a entender padrões, distribuições e relações entre as variáveis do conjunto de dados.

---

### src/bayes.py
Implementa o cálculo da probabilidade condicional utilizando o Teorema de Bayes.

O resultado principal é a probabilidade de um cliente ser inadimplente dado que ele já atrasou um pagamento.

---

### main.py
Arquivo principal que orquestra a execução do projeto, realizando:
- Carregamento dos dados
- Tratamento
- Análise exploratória
- Cálculo Bayesiano

---

## 📊 Análise Exploratória — Interpretação dos Gráficos

As imagens abaixo devem ser adicionadas na pasta img/ e referenciadas neste README.

### 📌 Distribuição de Inadimplência

!Distribuição de Inadimplência


Este gráfico mostra a quantidade de clientes inadimplentes e não inadimplentes.

É possível observar que a maioria dos clientes não é inadimplente, o que representa um cenário realista de dados de crédito e justifica o uso de análise probabilística.

---

### 📌 Score de Crédito vs Inadimplência

!Score vs Inadimplência


Este gráfico mostra a relação entre o score de crédito e a inadimplência.

Clientes inadimplentes tendem a apresentar scores mais baixos, porém há sobreposição entre os grupos, indicando que o score sozinho não é suficiente para determinar o risco.

---

### 📌 Renda Mensal vs Inadimplência

!Renda vs Inadimplência


O gráfico evidencia que clientes inadimplentes tendem a ter renda um pouco menor, mas também existem clientes com renda mais alta que se tornam inadimplentes.

Isso reforça a necessidade de uma análise baseada em probabilidade, e não em regras fixas.

---

## ▶️ Como Executar o Projeto

```bash
python data/gerar_dados.py
python main.py
```

---

## 🎯 Conclusão
Este projeto demonstra, de forma simples e objetiva, como a Aprendizagem Bayesiana pode ser aplicada em problemas reais de análise de crédito.

Ele serve como uma base sólida para evolução futura, como a implementação de Naive Bayes com scikit-learn ou modelos mais avançados de classificação.
