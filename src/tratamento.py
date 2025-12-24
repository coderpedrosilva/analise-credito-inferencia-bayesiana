def tratar_dados(df):
    df.loc[df["idade"] > 100, "idade"] = df["idade"].median()

    df.loc[df["renda_mensal"] < 0, "renda_mensal"] = df["renda_mensal"].median()
    df.loc[df["valor_emprestimo"] < 0, "valor_emprestimo"] = df["valor_emprestimo"].median()

    df.loc[df["score_credito"] < 300, "score_credito"] = df["score_credito"].median()

    return df
