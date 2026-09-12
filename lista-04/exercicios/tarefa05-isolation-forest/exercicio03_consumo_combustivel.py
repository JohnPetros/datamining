"""Exercício 3 — detecção de consumo de combustível incomum.

As duas características são analisadas juntas: distância percorrida e litros
consumidos. A combinação [100, 20.0] foge do padrão observado nas demais
viagens.
"""

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


consumo = [
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0],
]

modelo = IsolationForest(
    n_estimators=5,
    contamination=0.1,
    random_state=42,
)

rotulos = modelo.fit_predict(consumo)

print("Distância (km), litros -> classificação")
for (distancia, litros), rotulo in zip(consumo, rotulos):
    classificacao = "Candidato a outlier" if rotulo == -1 else "Normal"
    print(f"{distancia}, {litros} -> {classificacao}")

normais = [
    (distancia, litros)
    for (distancia, litros), rotulo in zip(consumo, rotulos)
    if rotulo == 1
]
outliers = [
    (distancia, litros)
    for (distancia, litros), rotulo in zip(consumo, rotulos)
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
    for distancia, litros in outliers:
        plt.annotate(
            f"({distancia}, {litros})",
            (distancia, litros),
            textcoords="offset points",
            xytext=(6, 6),
        )

plt.xlabel("Distância percorrida (km)")
plt.ylabel("Litros consumidos")
plt.title("Consumo de combustível")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(
    "\nA distância e os litros devem ser analisados juntos porque o consumo "
    "depende da relação entre essas duas características."
)
