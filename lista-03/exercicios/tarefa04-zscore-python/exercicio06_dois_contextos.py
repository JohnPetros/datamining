"""Exercício 6 — o mesmo valor em dois contextos.

O valor 110 está 10 unidades acima da média nos dois grupos, mas os grupos
possuem desvios-padrão diferentes. O Z-Score permite comparar essa distância
em relação à dispersão de cada grupo.
"""

media_a = 100
desvio_a = 2
media_b = 100
desvio_b = 20
valor = 110

distancia_a = valor - media_a
distancia_b = valor - media_b
z_a = distancia_a / desvio_a
z_b = distancia_b / desvio_b

print(f"Valor analisado: {valor}")
print(f"Distância absoluta nos dois grupos: {distancia_a}")
print(f"Grupo A -> Z-Score: {z_a:.2f}")
print(f"Grupo B -> Z-Score: {z_b:.2f}")

print("\nComparação:")
print(
    f"No Grupo A, {valor} está {z_a:.0f} desvios-padrão acima da média "
    "e é muito incomum."
)
print(
    f"No Grupo B, {valor} está apenas {z_b:.1f} desvio-padrão acima da média "
    "e é relativamente comum."
)
print(
    "A mesma distância absoluta de 10 unidades pode ser incomum em um grupo "
    "e comum em outro porque a dispersão dos grupos é diferente."
)
