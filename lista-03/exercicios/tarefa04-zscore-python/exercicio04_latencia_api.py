"""Exercício 4 — análise de latência de uma API.

Calcula a média e o desvio-padrão das latências e verifica se a leitura de
180 ms merece investigação pela regra prática |Z| > 3.

Resultado esperado:
    média ≈ 110,00 ms
    desvio-padrão ≈ 26,52 ms
    Z-Score de 180 ms ≈ 2,64
    180 ms não ultrapassa |Z| > 3.

Mesmo quando um valor é apontado como candidato, investigar não significa
apagá-lo automaticamente.
"""

import numpy as np


latencias = [98, 102, 101, 99, 100, 103, 97, 180]
valor_analisado = 180

media = np.mean(latencias)
desvio = np.std(latencias)
z_score = (valor_analisado - media) / desvio
merece_investigacao = abs(z_score) > 3

print(f"Latências: {latencias}")
print(f"Média: {media:.2f} ms")
print(f"Desvio-padrão: {desvio:.2f} ms")
print(f"Valor analisado: {valor_analisado} ms")
print(f"Z-Score: {z_score:.2f}")

if merece_investigacao:
    print(f"A latência {valor_analisado} ms merece investigação (|Z| > 3).")
else:
    print(f"A latência {valor_analisado} ms não ultrapassa |Z| > 3.")

print("Investigar não significa apagar automaticamente o valor.")
