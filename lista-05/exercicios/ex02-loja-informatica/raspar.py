import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    produtos = soup.select("article.produto")
    if not produtos:
        raise ValueError("Nenhum produto foi encontrado na página.")

    dados = []
    for produto in produtos:
        item = {
            "nome": produto.select_one(".nome").get_text(strip=True),
            "fabricante": produto.select_one(".fabricante").get_text(strip=True),
            "categoria": produto.select_one(".categoria").get_text(strip=True),
            "preco": produto.select_one(".preco").get_text(strip=True),
            "estoque": produto.select_one(".estoque").get_text(strip=True),
        }
        dados.append(item)
        print(f"{item['nome']} | {item['fabricante']} | {item['categoria']} | R$ {item['preco']} | {item['estoque']}")

    print("\nProdutos disponíveis:")
    for item in dados:
        if item["estoque"] == "Disponível":
            print(f"- {item['nome']} — R$ {item['preco']}")


if __name__ == "__main__":
    main()
