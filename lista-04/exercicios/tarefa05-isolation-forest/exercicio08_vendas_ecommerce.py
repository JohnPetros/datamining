"""Exercício 8 — detecção de anomalias em vendas de e-commerce.

O identificador da venda não participa do modelo. As características usadas
são valor total, quantidade de itens e percentual de desconto.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest


arquivo = (
    Path(__file__).resolve().parents[2]
    / "dados"
    / "vendas_ecommerce.csv"
)
dados = pd.read_csv(arquivo)

print("Primeiras linhas:")
print(dados.head())

caracteristicas = [
    "valor_total",
    "quantidade_itens",
    "desconto_percentual",
]

modelo = IsolationForest(
    n_estimators=100,
    contamination=0.15,
    random_state=42,
)
dados["rotulo"] = modelo.fit_predict(dados[caracteristicas])

candidatos = dados[dados["rotulo"] == -1]

print("\nVendas candidatas:")
print(candidatos.to_string(index=False))

print("\nIdentificadores sinalizados:")
print(candidatos["id_venda"].to_list())

print("\nAvaliação dos casos:")
print(
    "- V011: valor muito alto, poucos itens e desconto de 90%; pode ser "
    "uma promoção legítima ou um erro, e precisa ser investigada."
)
print(
    "- V017: valor baixo para 25 itens; pode representar uma promoção "
    "especial, um erro de preço ou uma inconsistência nos dados."
)
print(
    "- V020: valor alto, poucos itens e desconto de 85%; pode ser uma venda "
    "de alto valor com promoção ou exigir investigação."
)

normais = dados[dados["rotulo"] == 1]
plt.figure(figsize=(9, 5))
plt.scatter(
    normais["quantidade_itens"],
    normais["valor_total"],
    color="steelblue",
    label="Normal",
)
plt.scatter(
    candidatos["quantidade_itens"],
    candidatos["valor_total"],
    color="crimson",
    marker="x",
    s=100,
    label="Candidato a outlier",
)
for _, venda in candidatos.iterrows():
    plt.annotate(
        venda["id_venda"],
        (venda["quantidade_itens"], venda["valor_total"]),
        textcoords="offset points",
        xytext=(6, 6),
    )

plt.xlabel("Quantidade de itens")
plt.ylabel("Valor total")
plt.title("Vendas de comércio eletrônico")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
