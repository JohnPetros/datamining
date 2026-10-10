import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")
CATEGORIA_ESCOLHIDA = "Tecnologia"


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    noticias = soup.select("article.noticia")
    if not noticias:
        raise ValueError("Nenhuma notícia foi encontrada na página.")

    for noticia in noticias:
        dados = {
            "categoria": noticia.select_one(".categoria").get_text(strip=True),
            "titulo": noticia.select_one(".titulo").get_text(strip=True),
            "data": noticia.select_one("time.data").get_text(strip=True),
            "resumo": noticia.select_one(".resumo").get_text(strip=True),
            "autor": noticia.select_one(".autor").get_text(strip=True),
        }
        print(f"\n[{dados['categoria']}] {dados['titulo']}\nData: {dados['data']} | Autor: {dados['autor']}\n{dados['resumo']}")

    print(f"\nTítulos da categoria {CATEGORIA_ESCOLHIDA}:")
    for noticia in noticias:
        categoria = noticia.select_one(".categoria").get_text(strip=True)
        if categoria.casefold() == CATEGORIA_ESCOLHIDA.casefold():
            print(f"- {noticia.select_one('.titulo').get_text(strip=True)}")


if __name__ == "__main__":
    main()
