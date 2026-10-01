"""Gera uma base fictícia e seu gabarito separado, com semente fixa."""
from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent


def gerar():
    rng = np.random.default_rng(42)
    registros = []
    for i in range(120):
        categoria = rng.choice(['papelaria', 'casa', 'eletronicos'])
        preco = {'papelaria': 35, 'casa': 100, 'eletronicos': 250}[categoria]
        quantidade = int(rng.integers(1, 6))
        desconto = int(rng.choice([0, 5, 10, 15]))
        valor = round(preco * quantidade * rng.uniform(0.85, 1.15) * (1 - desconto / 100), 2)
        hora = int(rng.choice([3, 9, 10, 12, 14, 16, 18, 20, 22], p=[.04,.10,.12,.16,.16,.12,.12,.10,.08]))
        data = pd.Timestamp('2026-09-01') + pd.Timedelta(days=i // 4, hours=hora, minutes=int(rng.integers(0,60)))
        registros.append([f'T{i+1:03}', data, valor, quantidade, desconto, categoria,
                          rng.choice(['BR', 'PT'], p=[.9,.1]), rng.choice(['pix', 'cartao', 'boleto'], p=[.45,.45,.1])])
    # Casos especificados antes de treinar o modelo, sem buscar o melhor resultado.
    casos = [
        [8000, 1, 0, 'eletronicos', 'BR', 'cartao', 14, 'valor_extremo', 'R$ 8.000 por um item, muito acima do padrão da loja.'],
        [180, 45, 5, 'papelaria', 'BR', 'pix', 10, 'quantidade_extrema', '45 itens em uma compra, contra 1 a 5 nas compras usuais.'],
        [300, 2, 95, 'casa', 'BR', 'cartao', 16, 'desconto_extremo', 'Desconto de 95%, fora da política simulada de até 15%.'],
        [1100, 1, 5, 'papelaria', 'PT', 'cartao', 3, 'combinacao', 'Valor e quantidade dentro das faixas globais, mas R$ 1.100 por um item de papelaria é incompatível com o padrão da categoria.'],
        [45, 4, 10, 'eletronicos', 'BR', 'pix', 12, 'combinacao', 'R$ 45 por quatro eletrônicos: valor por item muito baixo para a categoria.'],
        [170, 2, 5, 'casa', 'PT', 'cartao', 3, 'indevida_sem_desvio', 'Compra confirmada como indevida no cenário fictício; atributos comuns podem não revelar o caso ao modelo.'],
    ]
    gabarito = []
    for i, (valor, qtd, desconto, cat, pais, pagamento, hora, tipo, descricao) in enumerate(casos, 121):
        identificador = f'T{i:03}'
        registros.append([identificador, pd.Timestamp('2026-09-30') + pd.Timedelta(hours=hora), valor, qtd, desconto, cat, pais, pagamento])
        gabarito.append([identificador, tipo, descricao, tipo != 'indevida_sem_desvio'])
    df = pd.DataFrame(registros, columns=['id_transacao', 'data_hora', 'valor', 'quantidade', 'desconto_percentual', 'categoria', 'pais', 'pagamento'])
    for indice, coluna in [(11, 'valor'), (34, 'desconto_percentual'), (52, 'categoria'), (77, 'pagamento')]:
        df.loc[indice, coluna] = np.nan
    (BASE / 'dados').mkdir(parents=True, exist_ok=True)
    df.to_csv(BASE / 'dados/transacoes.csv', index=False)
    pd.DataFrame(gabarito, columns=['id_transacao', 'tipo', 'descricao', 'anomalia_observavel']).to_csv(BASE / 'dados/gabarito_anomalias.csv', index=False)
    print('Gerados 126 registros, 5 anomalias observáveis e 1 compra indevida sem desvio observável e 4 células ausentes.')


if __name__ == '__main__':
    gerar()
