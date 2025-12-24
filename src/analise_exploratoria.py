import matplotlib.pyplot as plt
import seaborn as sns

def analise_exploratoria(df):
    sns.countplot(x="inadimplente", data=df)
    plt.title("Distribuição de Inadimplência")
    plt.show()

    sns.boxplot(x="inadimplente", y="score_credito", data=df)
    plt.title("Score de Crédito vs Inadimplência")
    plt.show()

    sns.boxplot(x="inadimplente", y="renda_mensal", data=df)
    plt.title("Renda Mensal vs Inadimplência")
    plt.show()
