import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    livros = soup.select("article.livro")
    if not livros:
        raise ValueError("Nenhum livro foi encontrado na página.")

    disponiveis = []
    for livro in livros:
        palavras = [item.get_text(strip=True) for item in livro.select(".palavras-chave li")]
        dados = {
            "titulo": livro.select_one(".titulo").get_text(strip=True),
            "autor": livro.select_one(".autor").get_text(strip=True),
            "ano": livro.select_one(".ano").get_text(strip=True),
            "genero": livro.select_one(".genero").get_text(strip=True),
            "situacao": livro.select_one(".situacao").get_text(strip=True),
            "palavras": palavras,
        }
        print(f"\n{dados['titulo']} ({dados['ano']}) — {dados['autor']}\nGênero: {dados['genero']} | Situação: {dados['situacao']}\nPalavras-chave: {', '.join(palavras)}")
        if dados["situacao"].casefold() == "disponível".casefold():
            disponiveis.append(dados)

    print("\nLivros disponíveis para empréstimo:")
    for livro in disponiveis:
        print(f"- {livro['titulo']} — {livro['autor']}")


if __name__ == "__main__":
    main()
