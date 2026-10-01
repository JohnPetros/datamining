# Trabalho — Isolation Forest

Grupo 4: Thiago Martins, Gabriel da Silva, Kauan Fonseca, João Pedro Carvalho e João Gabriel, conforme a apresentação fornecida.

## Entregáveis

- `apresentacao/Isolation_Forest_Grupo4_completo.pptx`: apresentação de 20 slides, baseada no PPT original, com resultados e referências.
- `apresentacao/Isolation_Forest_Grupo4_completo.pdf`: versão para leitura e compartilhamento, com o novo design.
- `isolation_forest_loja_online.ipynb`: notebook executado, com explicações, saídas e três gráficos.
- `dados/transacoes.csv`: base fictícia usada pelo modelo.
- `dados/gabarito_anomalias.csv`: cinco anomalias observáveis e um caso de compra indevida sem desvio observável, usados somente na avaliação.
- `resultados/`: gráficos, transações avaliadas, métricas e análise de sensibilidade.
- `gerar_dados.py`: geração reproduzível da base, com semente 42.
- `enunciado/Trabalhos_25092026.pdf`: enunciado do trabalho.

## Cenário e requisitos

Uma loja online vende itens de papelaria, casa e eletrônicos. O objetivo é priorizar compras incomuns para investigação, sem tratar toda anomalia como fraude.

| Requisito | Implementação |
|---|---|
| Pelo menos 50 registros | 126 transações |
| Identificador | `id_transacao`, único |
| Data ou período | `data_hora`, setembro de 2026 |
| Três características numéricas | `valor`, `quantidade`, `desconto_percentual` |
| Uma característica categórica | `categoria`, `pais`, `pagamento` |
| Três situações anormais conhecidas | Cinco anomalias, T121 a T125; T126 é uma compra indevida sem desvio observável |
| Dois valores ausentes | Quatro células, T012, T035, T053 e T078 |
| Anomalia por combinação | T124 e T125: preço por item incompatível com a categoria |
| Inspeção e tratamento | Pandas, tipos, estatísticas, mediana por categoria e moda |
| Novos atributos | Hora, seno/cosseno da hora, valor por item e razão de preço por categoria |
| Modelo | Isolation Forest, 100 árvores, semente 42, `contamination=0.05` |
| Dois gráficos | Dispersão, histograma e matriz de confusão |
| Interpretação | Casos encontrados, não detectados e falsos positivos no notebook e PPT |

Os três preços-base da simulação são aproximadamente R$ 35, R$ 100 e R$ 250 por item. Há variação de preço e descontos. Valores extremos são preservados para análise. O país PT e o horário de 3h também aparecem em compras normais; não são rótulos de fraude.

## Resultados da execução

O modelo sinalizou **7 transações**, recuperou **4 de 5 anomalias observáveis** e produziu **3 falsos positivos**. Precisão: **57,1%**; recall: **80,0%**. O gabarito não participa do ajuste, e o parâmetro de 5% foi fixado antes da avaliação.

| Caso | Contexto | Resultado |
|---|---|---|
| T121 | R$ 8.000 por um eletrônico | Detectado |
| T122 | 45 itens em uma compra | Detectado |
| T123 | Desconto de 95% | Detectado |
| T124 | R$ 1.100 por um item de papelaria | Detectado |
| T125 | R$ 45 por quatro eletrônicos | Não detectado |
| T126 | Compra indevida no cenário, com atributos usuais | Sem alerta; discussão qualitativa separada |

T049, T058 e T088 são falsos positivos: compras legítimas em PT com combinações relativamente raras. Aumentar `contamination` de 5% para 10% ampliou os alertas de 7 para 13, manteve os quatro acertos e elevou os falsos positivos de 3 para 9.

T125 mostra que uma razão de preço baixa não garante isolamento suficiente para ultrapassar o limiar do conjunto. T126 mostra que uma compra indevida pode ter características comuns. Por isso, ele não conta como falso negativo de anomalia estatística: o gabarito mantém seis casos documentados, mas a coluna `anomalia_observavel` seleciona apenas T121–T125 para a avaliação quantitativa. O recorte é definido pelo conceito de anomalia, sem alterar os parâmetros ou os sete alertas do modelo. Essas são interpretações das características e dos scores observados, não explicações causais produzidas pelo modelo.

As métricas usam uma base sintética e os mesmos registros do ajuste. Elas descrevem esta demonstração; não representam desempenho em compras futuras ou fraudes reais. A imputação por moda e a codificação de categorias também podem influenciar o resultado. Uma aplicação real exigiria validação temporal, pré-processamento preservado e revisão dos alertas por pessoas que conhecem o negócio.

## Executar

Use o ambiente Conda do repositório e abra o notebook:

```bash
conda activate datamining
jupyter lab trabalho-isolation-forest/isolation_forest_loja_online.ipynb
```

Selecione um kernel do ambiente `datamining` e execute as células em ordem. O notebook já contém as saídas verificadas e também salva os arquivos na pasta `resultados/`.

O CSV está pronto para uso. Caso seja necessário recriar a base fictícia com a mesma semente:

```bash
python trabalho-isolation-forest/gerar_dados.py
```

Versões da análise verificada: Python 3.12.13, Pandas 3.0.5 e scikit-learn 1.9.0. Versões diferentes podem produzir scores diferentes; os arquivos em `resultados/` registram a execução usada no PPT.

## Fontes

- [Isolation Forest — Liu, Ting e Zhou (2008)](https://doi.org/10.1109/ICDM.2008.17).
- [Isolation-Based Anomaly Detection — Liu, Ting e Zhou (2012)](https://doi.org/10.1145/2133360.2133363).
- [API oficial do IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html).
- [Histórico oficial do scikit-learn 0.18](https://scikit-learn.org/0.18/whats_new.html).
- [Caso CERN OpenStack — Metaj (2022)](https://repository.cern/records/4pbhe-e1w97): sistema com Isolation Forest e dois autoencoders; a tese relata AUC-ROC acima de 0,95 para cada modelo na avaliação do estudo.
- [Extended Isolation Forest](https://arxiv.org/abs/1811.02141).
- [Deep Isolation Forest](https://arxiv.org/abs/2206.06602).
