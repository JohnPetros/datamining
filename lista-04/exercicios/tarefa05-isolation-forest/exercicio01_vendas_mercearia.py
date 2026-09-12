"""Exercício 1 — detecção de anomalia em vendas de uma mercearia.

O valor 400 pode representar uma promoção, uma encomenda excepcional ou um
erro de registro. Por isso, o modelo apenas sinaliza o valor para investigação;
ele não deve ser removido automaticamente.
"""

from sklearn.ensemble import IsolationForest


vendas = [
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400],
]

modelo = IsolationForest(
    n_estimators=5,
    contamination=0.1,
    random_state=42,
)

rotulos = modelo.fit_predict(vendas)

print("Valor -> classificação")
for [valor], rotulo in zip(vendas, rotulos):
    classificacao = "Candidato a outlier" if rotulo == -1 else "Normal"
    print(f"{valor} -> {classificacao}")

print("\nPergunta para discussão:")
print(
    "O valor 400 não deve ser removido automaticamente. É necessário "
    "investigar se ele representa uma promoção, uma encomenda ou um erro."
)
