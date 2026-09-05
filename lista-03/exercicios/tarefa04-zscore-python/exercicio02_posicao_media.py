"""Exercício 2 — identificar a posição dos valores em relação à média.

Dados:
    casos = [85, 100, 120]
    média = 100
    desvio-padrão = 10

Resultados esperados:
    85  -> Z-Score -1,50 -> abaixo da média
    100 -> Z-Score  0,00 -> exatamente na média
    120 -> Z-Score  2,00 -> acima da média

Interpretação do sinal:
    Z-Score negativo: abaixo da média.
    Z-Score igual a zero: igual à média.
    Z-Score positivo: acima da média.
"""

casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z_score = (valor - media) / desvio

    if z_score < 0:
        posicao = "abaixo da média"
    elif z_score > 0:
        posicao = "acima da média"
    else:
        posicao = "exatamente na média"

    print(f"{valor} -> Z-Score: {z_score:.2f} -> {posicao}")

print("\nInterpretação do sinal:")
print("- Z-Score negativo: o valor está abaixo da média.")
print("- Z-Score igual a zero: o valor é igual à média.")
print("- Z-Score positivo: o valor está acima da média.")
