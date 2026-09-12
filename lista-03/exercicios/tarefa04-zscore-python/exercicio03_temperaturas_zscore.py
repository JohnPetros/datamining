"""Exercício 3 — identificar a leitura mais incomum.

Dados:
    temperaturas = [21, 23, 25, 27, 29]
    média = 25
    desvio-padrão = 2

O maior valor absoluto de Z indica a leitura mais distante da média em
termos de desvios-padrão.
"""

temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

resultados = []

for temperatura in temperaturas:
    z_score = (temperatura - media) / desvio
    resultados.append((temperatura, z_score))
    print(f"{temperatura} -> Z-Score: {z_score:.2f}")

maior_distancia = max(abs(z_score) for _, z_score in resultados)
mais_incomuns = [
    (temperatura, z_score)
    for temperatura, z_score in resultados
    if abs(z_score) == maior_distancia
]

print(f"\nMaior distância da média: |Z| = {maior_distancia:.2f}")
for temperatura, z_score in mais_incomuns:
    print(f"Leitura mais incomum: {temperatura}°C (Z = {z_score:.2f})")
