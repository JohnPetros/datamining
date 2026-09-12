"""Exercício 9 — comparação entre IQR e Z-Score.

O valor 30 é analisado por duas técnicas diferentes. O IQR usa os quartis e
a dispersão central; o Z-Score usa a média e o desvio-padrão.
"""

import numpy as np


dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]
valor_analisado = 30

q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

media = np.mean(dados)
desvio = np.std(dados)
z_score = (valor_analisado - media) / desvio

classificado_iqr = (
    valor_analisado < limite_inferior
    or valor_analisado > limite_superior
)
classificado_z_score = abs(z_score) > 3

print(f"Dados: {dados}")
print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Limite inferior do IQR: {limite_inferior:.2f}")
print(f"Limite superior do IQR: {limite_superior:.2f}")
print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Z-Score de {valor_analisado}: {z_score:.2f}")
print(f"IQR aponta {valor_analisado} como candidato? {classificado_iqr}")
print(
    f"Z-Score aponta {valor_analisado} como candidato (|Z| > 3)? "
    f"{classificado_z_score}"
)

print("\nConclusão:")
print(
    "O IQR aponta 30 como candidato a outlier, pois ele ultrapassa o "
    "limite superior de 17."
)
print(
    "O Z-Score resulta em aproximadamente 2,74 e não ultrapassa o limite "
    "prático de 3."
)
print(
    "As técnicas podem chegar a conclusões diferentes porque analisam o "
    "mesmo dado por critérios diferentes."
)
