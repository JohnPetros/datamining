"""Exercício 7 — função para interpretar um Z-Score."""


def interpretar_z(z):
    """Classifica um Z-Score conforme a regra prática da lista."""
    if abs(z) > 3:
        return "Investigar"
    if z < 0:
        return "Abaixo da média"
    if z > 0:
        return "Acima da média"
    return "Na média"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

for z_score in valores_z:
    classificacao = interpretar_z(z_score)
    print(f"{z_score:.1f} -> {classificacao}")
