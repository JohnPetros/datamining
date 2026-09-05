"""Exercício 1 — distância em passos de desvio-padrão.

Dados:
    média = 100
    desvio-padrão = 5
    valor = 115

Resultado esperado:
    distância = 15
    Z-Score = 3

Interpretação: o valor está 15 unidades e 3 desvios-padrão acima da média.
Como |Z| = 3, o valor merece investigação, mas não deve ser apagado
automaticamente.
"""

media = 100
desvio = 5
valor = 115

distancia = valor - media
distancia_absoluta = abs(distancia)
z_score = distancia / desvio

print(f"Média: {media}")
print(f"Desvio-padrão: {desvio}")
print(f"Valor analisado: {valor}")
print(f"Distância até a média: {distancia_absoluta}")
print(f"Z-Score: {z_score:.2f}")
print(
    f"O valor {valor} está {abs(z_score):.0f} desvios-padrão "
    f"acima da média."
)
