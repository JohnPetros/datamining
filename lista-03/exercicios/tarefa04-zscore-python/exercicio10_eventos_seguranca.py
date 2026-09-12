"""Exercício 10 — mini-análise de eventos de segurança.

O Z-Score ajuda a apontar eventos que merecem investigação. Em segurança,
um evento incomum pode ser justamente o sinal mais importante do conjunto.
"""

import pandas as pd


dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40],
}

df = pd.DataFrame(dados)

media = df["Tentativas_Login"].mean()
# ddof=0 mantém o mesmo padrão de desvio-padrão populacional usado nos
# exercícios anteriores.
desvio = df["Tentativas_Login"].std(ddof=0)

df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio
df["Status"] = df["Z_Score"].abs().apply(
    lambda z: "Investigar" if z > 3 else "Comum"
)

print(f"Média de tentativas: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print("\nEventos analisados:")
print(df.to_string(index=False, formatters={"Z_Score": "{:.2f}".format}))

print("\nEventos com |Z| > 3:")
eventos_para_investigar = df[df["Status"] == "Investigar"]
if eventos_para_investigar.empty:
    print("Nenhum evento ultrapassou |Z| > 3.")
else:
    print(
        eventos_para_investigar.to_string(
            index=False,
            formatters={"Z_Score": "{:.2f}".format},
        )
    )

print(
    "\nEm segurança, um evento incomum pode ser o dado mais importante da "
    "análise, pois pode indicar uma tentativa de invasão ou outro incidente."
)
