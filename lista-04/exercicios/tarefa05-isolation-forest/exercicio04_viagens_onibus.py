"""Exercício 4 — detecção de viagem incomum em ônibus urbano.

As características são quantidade de passageiros e atraso em minutos. A
combinação [10, 45] foge do padrão das demais viagens.
"""

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


viagens = [
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45],
]

modelo = IsolationForest(
    n_estimators=5,
    contamination=0.1,
    random_state=42,
)

rotulos = modelo.fit_predict(viagens)

print("Passageiros, atraso (min) -> classificação")
for (passageiros, atraso), rotulo in zip(viagens, rotulos):
    classificacao = "Candidato a outlier" if rotulo == -1 else "Normal"
    print(f"{passageiros}, {atraso} -> {classificacao}")

normais = [
    (passageiros, atraso)
    for (passageiros, atraso), rotulo in zip(viagens, rotulos)
    if rotulo == 1
]
outliers = [
    (passageiros, atraso)
    for (passageiros, atraso), rotulo in zip(viagens, rotulos)
    if rotulo == -1
]

plt.figure(figsize=(8, 5))
if normais:
    x_normais, y_normais = zip(*normais)
    plt.scatter(x_normais, y_normais, color="steelblue", label="Normal")
if outliers:
    x_outliers, y_outliers = zip(*outliers)
    plt.scatter(
        x_outliers,
        y_outliers,
        color="crimson",
        marker="x",
        s=100,
        label="Candidato a outlier",
    )
    for passageiros, atraso in outliers:
        plt.annotate(
            f"({passageiros}, {atraso})",
            (passageiros, atraso),
            textcoords="offset points",
            xytext=(6, 6),
        )

plt.xlabel("Passageiros")
plt.ylabel("Atraso (minutos)")
plt.title("Viagens de ônibus urbano")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(
    "\nA viagem pode ter sido afetada por congestionamento, acidente ou "
    "falha mecânica. O modelo sinaliza o caso, mas não determina a causa."
)
