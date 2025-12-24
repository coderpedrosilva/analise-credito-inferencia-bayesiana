def probabilidade_bayesiana(df):
    p_inadimplente = df["inadimplente"].mean()
    p_atraso = df["atraso_pagamento"].mean()

    p_atraso_dado_inadimplente = (
        df[df["inadimplente"] == 1]["atraso_pagamento"].mean()
    )

    p_inadimplente_dado_atraso = (
        p_atraso_dado_inadimplente * p_inadimplente
    ) / p_atraso

    return p_inadimplente_dado_atraso
