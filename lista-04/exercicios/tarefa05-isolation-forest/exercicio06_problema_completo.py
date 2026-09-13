"""Exercício 6 — problema completo de detecção de anomalias.

Contexto: quantidade de acessos diários a um site. A maioria dos dias fica
entre 95 e 125 acessos, enquanto os valores 5 e 500 representam situações
incomuns que precisam ser investigadas.
"""

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


acessos = [
    [100], [110], [95], [120], [105], [115],
    [98], [125], [108], [102], [118], [112],
    [104], [99], [121], [5], [500],
]

quantidade_candidatos = 2
modelo = IsolationForest(
    n_estimators=5,
    contamination=quantidade_candidatos / len(acessos),
    random_state=42,
)

rotulos = modelo.fit_predict(acessos)
candidatos = [
    (dia, acessos[dia - 1][0])
    for dia, rotulo in enumerate(rotulos, start=1)
    if rotulo == -1
]

print("Dia -> acessos -> classificação")
for dia, ([quantidade], rotulo) in enumerate(zip(acessos, rotulos), start=1):
    classificacao = "Candidato a outlier" if rotulo == -1 else "Normal"
    print(f"{dia} -> {quantidade} -> {classificacao}")

print(f"\nCandidatos encontrados: {candidatos}")
print("\nAnálise dos candidatos:")
print(
    "- 5 acessos: pode indicar manutenção, indisponibilidade do site ou "
    "falha na coleta; deve ser investigado."
)
print(
    "- 500 acessos: pode indicar uma campanha legítima, divulgação do site "
    "ou tráfego automatizado; deve ser investigado."
)
print(
    "Critério utilizado: os valores foram considerados incomuns por estarem "
    "isolados em relação ao padrão da maioria dos dias."
)

dias = range(1, len(acessos) + 1)
cores = ["crimson" if rotulo == -1 else "steelblue" for rotulo in rotulos]

plt.figure(figsize=(9, 5))
plt.scatter(dias, [quantidade[0] for quantidade in acessos], c=cores, s=70)
for dia, quantidade in candidatos:
    plt.annotate(
        f"{quantidade}",
        (dia, quantidade),
        textcoords="offset points",
        xytext=(6, 6),
    )
plt.xlabel("Dia da observação")
plt.ylabel("Quantidade de acessos")
plt.title("Acessos diários ao site")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
