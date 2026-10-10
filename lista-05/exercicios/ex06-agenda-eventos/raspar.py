import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    eventos = soup.select("article.evento")
    if not eventos:
        raise ValueError("Nenhum evento foi encontrado na página.")

    print("Agenda de eventos:")
    for evento in eventos:
        palestrantes = [p.get_text(strip=True) for p in evento.select(".palestrante")]
        link = evento.select_one("a.inscricao")
        print(f"\n{evento.select_one('.nome').get_text(strip=True)}")
        print(f"Data: {evento.select_one('time.data').get_text(strip=True)} | Horário: {evento.select_one('.horario').get_text(strip=True)}")
        print(f"Local: {evento.select_one('.local').get_text(strip=True)}")
        print(f"Palestrantes ({len(palestrantes)}): {', '.join(palestrantes)}")
        print(f"Inscrição: {link.get_text(strip=True)} — {link.get('href')}")
        if len(palestrantes) > 1:
            print("Este evento possui mais de um palestrante.")


if __name__ == "__main__":
    main()
