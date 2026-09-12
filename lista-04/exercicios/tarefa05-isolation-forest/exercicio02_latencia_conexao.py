"""Exercício 2 — detecção de latências incomuns.

As medições normais ficam principalmente entre 20 e 70 ms. As medições de
220 ms e 280 ms foram incluídas para representar possíveis anomalias.
"""

from sklearn.ensemble import IsolationForest


latencias = [
    [32], [45], [28], [50], [41], [35], [60],
    [55], [47], [39], [220], [280], [65], [25],
]

quantidade_candidatos = 2
contaminacao = quantidade_candidatos / len(latencias)

modelo = IsolationForest(
    n_estimators=5,
    contamination=contaminacao,
    random_state=42,
)

rotulos = modelo.fit_predict(latencias)

print("Latência (ms) -> classificação")
for [latencia], rotulo in zip(latencias, rotulos):
    classificacao = "Candidato a outlier" if rotulo == -1 else "Normal"
    print(f"{latencia} -> {classificacao}")

print("\nPergunta para discussão:")
print(
    "Uma latência alta não representa necessariamente uma falha. Ela pode "
    "ser causada por congestionamento, distância até o servidor, carga do "
    "serviço ou uma medição pontual. O contexto deve ser investigado."
)
