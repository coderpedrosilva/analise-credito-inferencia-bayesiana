# 📊 Análise de Crédito com Inferência Bayesiana

## 📌 Visão Geral
Este projeto aplica conceitos de Inferência Bayesiana, utilizando o Teorema de Bayes para estimar probabilidades condicionais a partir de dados observados.

O foco é demonstrar, de forma prática e didática, como a **probabilidade condicional** pode auxiliar na tomada de decisão em cenários reais, como a identificação de clientes com maior risco de inadimplência.

Projeto de nível **júnior**, voltado para estudos iniciais em Ciência de Dados, Estatística e Machine Learning.

## ▶️ Como Executar o Projeto

```bash
python data/gerar_dados.py
python main.py
```

---

## 🧠 Conceito: Inferência Bayesiana

A Inferência Bayesiana é baseada no **Teorema de Bayes**, que permite estimar probabilidades condicionais a partir de evidências observadas.

De forma simples, este projeto responde à seguinte pergunta:

> Qual é a probabilidade de um cliente ser inadimplente dado que ele já atrasou um pagamento?

Embora não haja treino de um modelo de Machine Learning, o projeto demonstra o princípio do aprendizado Bayesiano, no qual probabilidades são estimadas e atualizadas a partir de evidências observadas.

Essa abordagem é amplamente utilizada em:
- Análise de risco de crédito  
- Sistemas de apoio à decisão  
- Modelos probabilísticos  

---

## 📐 Teorema de Bayes (intuição e aplicação)

O Teorema de Bayes é definido por:

```
P(A | B) = P(B | A) · P(A)
           ----------------
                 P(B)
```
A forma abaixo é equivalente e mais próxima da implementação em código, facilitando a transição da teoria para o Python:

```
P(A | B) = (P(B | A) * P(A)) / P(B)
```

Onde:
- **P(A | B)**: probabilidade do evento A ocorrer dado B  
- **P(A)**: probabilidade inicial de A  
- **P(B | A)**: probabilidade de B ocorrer dado A  
- **P(B)**: probabilidade total de B ocorrer  

No contexto do projeto:
- **A** = cliente ser inadimplente  
- **B** = cliente ter atraso de pagamento  

A função `probabilidade_bayesiana(df)` implementa diretamente essa fórmula:

- `p_inadimplente` calcula **P(A)**, a taxa geral de inadimplência  
- `p_atraso` calcula **P(B)**, a taxa geral de atraso  
- `p_atraso_dado_inadimplente` calcula **P(B | A)**, a proporção de inadimplentes que atrasaram pagamentos  
- O cálculo final aplica o Teorema de Bayes para obter **P(A | B)**  

O valor retornado representa a **probabilidade de inadimplência dado que houve atraso de pagamento**, conectando a teoria estatística ao comportamento observado nos dados.

---

## 📁 Arquitetura do Projeto

```text
inferencia_bayesiana/
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

## 📄 Descrição dos Arquivos (Resumo)

- **data/gerar_dados.py**

Gera uma base de dados sintética de crédito, incluindo propositalmente inconsistências para demonstrar tratamento de dados.

- **data/credito.csv**

Base de dados utilizada em todas as etapas do projeto.

- **src/analise_exploratoria.py**

Executa a análise exploratória (EDA) e gera os gráficos do projeto.

- **src/bayes.py**

Implementa o cálculo da probabilidade condicional usando o Teorema de Bayes.

- **src/carregar_dados.py**

Responsável pela leitura do CSV e carregamento dos dados em um DataFrame pandas.

- **src/tratamento.py**

Realiza limpeza e correções, como valores negativos, idades irreais e scores fora do intervalo válido.

---

## 📈 Análise Estatística Descritiva

Após o tratamento dos dados, foi realizada uma análise estatística descritiva para compreender o perfil dos clientes e o comportamento das variáveis envolvidas no estudo de inadimplência.

### Estatísticas Resumidas

| Métrica | Idade | Renda Mensal | Valor do Empréstimo | Score de Crédito | Atraso de Pagamento | Inadimplente |
|--------|------:|-------------:|--------------------:|-----------------:|-------------------:|-------------:|
| Count  | 60.00 | 60.00 | 60.00 | 60.00 | 60.00 | 60.00 |
| Mean   | 43.48 | 3641.70 | 15027.51 | 560.14 | 0.25 | 0.22 |
| Std    | 15.33 | 1195.69 | 6048.52 | 163.00 | 0.44 | 0.42 |
| Min    | 19.00 | 1600.05 | 843.80 | 308.00 | 0.00 | 0.00 |
| 25%    | 31.75 | 2857.58 | 11865.30 | 433.00 | 0.00 | 0.00 |
| 50%    | 42.00 | 3626.68 | 13767.91 | 528.25 | 0.00 | 0.00 |
| 75%    | 56.25 | 4466.47 | 18788.98 | 707.00 | 0.25 | 0.00 |
| Max    | 69.00 | 7546.76 | 32774.14 | 846.00 | 1.00 | 1.00 |

### 📊 Análise Bayesiana

A probabilidade condicional foi calculada no arquivo `src/bayes.py`, utilizando contagens diretas dos eventos observados na base de dados.

Resultado obtido:

**P(Inadimplente | Atraso) = 26,67%**

### 📌 Interpretação

Esse valor significa que, entre os clientes que apresentaram atraso de pagamento, aproximadamente 26,67% tornaram-se inadimplentes.

O resultado mostra que o atraso é um forte indicativo de risco, mas não uma regra absoluta, reforçando a importância de modelos probabilísticos em vez de decisões determinísticas.

---

## 📊 Análise Exploratória — Interpretação dos Gráficos

### 📌 Distribuição de Inadimplência

![Distribuição de Inadimplência](img/img1.png)

Este gráfico mostra a quantidade de clientes inadimplentes e não inadimplentes.
Na variável inadimplente, os valores representam:

0 → cliente não inadimplente

1 → cliente inadimplente

É possível observar que a maioria dos clientes não é inadimplente, o que representa um cenário realista de dados de crédito e justifica o uso de análise probabilística.

---

### 📌 Score de Crédito vs Inadimplência

![Score vs Inadimplência](img/img2.png)

Este gráfico mostra a relação entre o score de crédito e a inadimplência.
No eixo horizontal, a variável inadimplente indica:

0 → cliente não inadimplente

1 → cliente inadimplente

Clientes inadimplentes tendem a apresentar scores mais baixos, porém há sobreposição entre os grupos, indicando que o score sozinho não é suficiente para determinar o risco.

As bolinhas fora da caixa azul representam outliers, indicando clientes com scores muito acima ou muito abaixo do padrão do grupo.
Esses casos mostram que existem exceções ao comportamento esperado, reforçando que o score de crédito, isoladamente, não determina a inadimplência.

---

### 📌 Renda Mensal vs Inadimplência

![Renda vs Inadimplência](img/img3.png)

O gráfico evidencia a relação entre renda mensal e inadimplência.
No eixo horizontal, a variável inadimplente representa:

0 → cliente não inadimplente

1 → cliente inadimplente

Clientes inadimplentes tendem a ter renda um pouco menor, mas também existem clientes com renda mais alta que se tornam inadimplentes.

As bolinhas fora da caixa azul representam outliers, ou seja, clientes com renda muito acima ou abaixo do padrão do grupo.
Esses casos indicam comportamentos atípicos e reforçam que a inadimplência não depende apenas da renda, mas da combinação de múltiplos fatores.

Isso reforça a necessidade de uma análise baseada em probabilidade, e não em regras fixas.

---

## 🎯 Conclusão
Este projeto demonstra, de forma simples e objetiva, como a Inferência Bayesiana pode ser aplicada para estimar riscos a partir de dados observados.

Ele serve como uma base sólida para evolução futura, como a implementação de Naive Bayes com scikit-learn ou modelos mais avançados de classificação.
