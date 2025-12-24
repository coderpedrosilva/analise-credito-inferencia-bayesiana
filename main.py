from src.carregar_dados import carregar_dados
from src.tratamento import tratar_dados
from src.analise_exploratoria import analise_exploratoria
from src.bayes import probabilidade_bayesiana

def main():
    df = carregar_dados("data/credito.csv")
    df = tratar_dados(df)

    print("Dados tratados com sucesso!\n")
    print(df.describe())

    analise_exploratoria(df)

    prob = probabilidade_bayesiana(df)
    print(f"\nProbabilidade de inadimplência dado atraso: {prob:.2%}")

if __name__ == "__main__":
    main()
