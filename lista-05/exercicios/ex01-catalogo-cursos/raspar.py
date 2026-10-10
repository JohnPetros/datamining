import os

import requests
from bs4 import BeautifulSoup


URL = os.getenv("SCRAPER_URL", "http://127.0.0.1:8000/")


def main():
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")

    cursos = soup.select("article.curso")
    if not cursos:
        raise ValueError("Nenhum curso foi encontrado na página.")

    for curso in cursos:
        nome = curso.select_one(".nome").get_text(strip=True)
        area = curso.select_one(".area").get_text(strip=True)
        carga = curso.select_one(".carga-horaria").get_text(strip=True)
        assuntos = [item.get_text(strip=True) for item in curso.select(".assuntos li")]
        print(f"\nCurso: {nome}\nÁrea: {area}\nCarga horária: {carga} horas")
        print("Assuntos estudados:")
        for assunto in assuntos:
            print(f"  - {assunto}")


if __name__ == "__main__":
    main()
