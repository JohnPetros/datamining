import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    secoes = soup.select("section.categoria-cardapio")
    if not secoes:
        raise ValueError("Nenhuma seção do cardápio foi encontrada.")

    for secao in secoes:
        categoria = secao.select_one("h2").get_text(strip=True)
        print(f"\n{categoria}")
        for item in secao.select("article.item"):
            nome = item.select_one(".nome").get_text(strip=True)
            descricao = item.select_one(".descricao").get_text(strip=True)
            preco = item.select_one(".preco").get_text(strip=True)
            print(f"- {nome} — {descricao} — R$ {preco}")


if __name__ == "__main__":
    main()
