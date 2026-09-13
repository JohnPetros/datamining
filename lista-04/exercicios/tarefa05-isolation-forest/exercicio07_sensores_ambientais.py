"""Exercício 7 — detecção de anomalias em sensores ambientais.

As características usadas pelo modelo são temperatura e umidade. O campo
``id_leitura`` é preservado apenas para identificar os registros sinalizados.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest


arquivo = (
    Path(__file__).resolve().parents[2]
    / "dados"
    / "sensores_ambientais.csv"
)
dados = pd.read_csv(arquivo)

print("Primeiras linhas:")
print(dados.head())

caracteristicas = ["temperatura", "umidade"]
modelo = IsolationForest(
    n_estimators=5,
    contamination=0.15,
    random_state=42,
)
dados["rotulo"] = modelo.fit_predict(dados[caracteristicas])

candidatos = dados[dados["rotulo"] == -1]

print("\nIdentificadores das leituras candidatas:")
print(candidatos["id_leitura"].to_list())
print("\nLeituras candidatas:")
print(candidatos.to_string(index=False))

normais = dados[dados["rotulo"] == 1]
plt.figure(figsize=(8, 5))
plt.scatter(
    normais["temperatura"],
    normais["umidade"],
    color="steelblue",
    label="Normal",
)
plt.scatter(
    candidatos["temperatura"],
    candidatos["umidade"],
    color="crimson",
    marker="x",
    s=100,
    label="Candidato a outlier",
)
for _, leitura in candidatos.iterrows():
    plt.annotate(
        leitura["id_leitura"],
        (leitura["temperatura"], leitura["umidade"]),
        textcoords="offset points",
        xytext=(6, 6),
    )

plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Sensores ambientais")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(
    "\nAs combinações sinalizadas fogem do padrão conjunto de temperatura "
    "e umidade observado nas demais leituras."
)
