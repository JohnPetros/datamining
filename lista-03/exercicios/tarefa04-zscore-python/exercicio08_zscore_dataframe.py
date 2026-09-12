"""Exercício 8 — cálculo de Z-Score em um DataFrame."""

import numpy as np
import pandas as pd


dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400],
}

df = pd.DataFrame(dados)

media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std(ddof=0)

df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar", "Comum")

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print("\nDataFrame completo:")
print(df.to_string(index=False, formatters={"Z_Score": "{:.2f}".format}))

print("\nLinhas marcadas para investigação:")
linhas_para_investigar = df[df["Status"] == "Investigar"]
if linhas_para_investigar.empty:
    print("Nenhuma linha ultrapassou |Z| > 3.")
else:
    print(
        linhas_para_investigar.to_string(
            index=False,
            formatters={"Z_Score": "{:.2f}".format},
        )
    )
