"""Exercício 5 — monitoramento de CPU com classificação.

Para cada leitura, calcula o Z-Score e classifica o valor como ``Comum`` ou
``Investigar``. A classificação usa a regra prática |Z| > 3.
"""

import numpy as np


cpu = [42, 45, 47, 44, 46, 43, 48, 92]

media = np.mean(cpu)
desvio = np.std(cpu)

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print("\nLeitura -> Z-Score -> classificação")

for leitura in cpu:
    z_score = (leitura - media) / desvio
    classificacao = "Investigar" if abs(z_score) > 3 else "Comum"
    print(f"{leitura} -> {z_score:.2f} -> {classificacao}")
