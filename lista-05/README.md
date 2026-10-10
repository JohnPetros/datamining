# Lista 05 — Web scraping com HTML, DOM e Beautiful Soup

Os seis exercícios usam páginas HTML locais com conteúdo fictício. Cada pasta
contém seu próprio `index.html` e script Python. Os scripts acessam a página por
HTTP em `127.0.0.1:8000`, usando `requests` e Beautiful Soup; nenhum site real é
consultado.

## Executar um exercício

Ative o ambiente Conda `datamining`. Em um terminal, entre na pasta do exercício
e inicie o servidor:

```bash
cd lista-05/exercicios/ex01-catalogo-cursos
python -m http.server --bind 127.0.0.1 8000
```

Deixe o servidor em execução. Em outro terminal, na raiz do repositório, execute:

```bash
conda activate datamining
python lista-05/exercicios/ex01-catalogo-cursos/raspar.py
```

Para fazer outro exercício, encerre o servidor atual com `Ctrl+C` e repita os
comandos usando a pasta correspondente. O servidor local sempre entrega o
`index.html` da pasta em que foi iniciado.

Se a porta `8000` estiver ocupada, inicie o servidor em outra porta, por exemplo
`8001`, e execute o script definindo `SCRAPER_URL=http://127.0.0.1:8001/`.

## Exercícios

1. `ex01-catalogo-cursos`: cursos, áreas, carga horária e assuntos.
2. `ex02-loja-informatica`: produtos e filtro de itens disponíveis.
3. `ex03-portal-noticias`: notícias e filtro por categoria.
4. `ex04-biblioteca`: livros, palavras-chave e filtro de disponibilidade.
5. `ex05-cardapio-categorias`: itens agrupados em pratos, bebidas e sobremesas.
6. `ex06-agenda-eventos`: eventos, links de inscrição e contagem de palestrantes.

As dependências `requests` e `beautifulsoup4` estão declaradas em
`environment.yml`.
