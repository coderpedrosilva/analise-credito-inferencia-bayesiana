import pandas as pd
import numpy as np

np.random.seed(42)

credito = pd.DataFrame({
    "idade": np.random.randint(18, 70, 60),
    "renda_mensal": np.random.normal(3500, 1200, 60).round(2),
    "valor_emprestimo": np.random.normal(15000, 7000, 60).round(2),
    "score_credito": np.random.randint(300, 850, 60),
    "atraso_pagamento": np.random.choice([0, 1], 60, p=[0.7, 0.3]),
    "inadimplente": np.random.choice([0, 1], 60, p=[0.75, 0.25])
})

# Inserindo erros propositalmente
credito.loc[5, "renda_mensal"] = -2000
credito.loc[12, "idade"] = 150
credito.loc[20, "score_credito"] = 50
credito.loc[33, "valor_emprestimo"] = -10000

# Salvar CSV
credito.to_csv("credito.csv", index=False)

print("Arquivo credito.csv criado com sucesso!")
