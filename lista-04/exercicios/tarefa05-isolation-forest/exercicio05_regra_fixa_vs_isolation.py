"""Exercício 5 — regra fixa versus Isolation Forest.

Regra manual escolhida para este contexto: consumo abaixo de 20 litros ou
acima de 100 litros é considerado incomum. Os limites são uma decisão do
analista e não uma regra universal.
"""

from sklearn.ensemble import IsolationForest


consumo_agua = [
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180],
]

limite_minimo = 20
limite_maximo = 100


def regra_fixa(consumo):
    """Retorna True quando o consumo está fora dos limites definidos."""
    return consumo < limite_minimo or consumo > limite_maximo


candidatos_regra = {
    consumo
    for [consumo] in consumo_agua
    if regra_fixa(consumo)
}

modelo = IsolationForest(
    n_estimators=5,
    contamination=2 / len(consumo_agua),
    random_state=42,
)
rotulos = modelo.fit_predict(consumo_agua)

candidatos_modelo = {
    consumo
    for [consumo], rotulo in zip(consumo_agua, rotulos)
    if rotulo == -1
}

print("Consumo -> regra fixa -> Isolation Forest")
for [consumo], rotulo in zip(consumo_agua, rotulos):
    resultado_regra = "Incomum" if regra_fixa(consumo) else "Comum"
    resultado_modelo = "Incomum" if rotulo == -1 else "Comum"
    print(f"{consumo} -> {resultado_regra} -> {resultado_modelo}")

print(f"\nCandidatos pela regra fixa: {sorted(candidatos_regra)}")
print(f"Candidatos pelo Isolation Forest: {sorted(candidatos_modelo)}")
print(f"Os candidatos são iguais? {candidatos_regra == candidatos_modelo}")

print("\nComparação:")
print(
    "A regra fixa é simples, transparente e fácil de aplicar, mas depende "
    "de limites definidos manualmente e pode não se adaptar a outros contextos."
)
print(
    "O Isolation Forest pode ser útil quando não existe um limite conhecido, "
    "pois aprende o padrão de isolamento dos dados."
)
print(
    "Não existe um método sempre melhor: a escolha depende do conhecimento "
    "do problema e da necessidade de explicação do resultado."
)
