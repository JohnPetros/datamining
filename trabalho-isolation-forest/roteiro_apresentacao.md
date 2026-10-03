# Roteiro da apresentação — Isolation Forest

Divisão para cinco integrantes, sem nomes. Tempo total estimado: 15 a 20 minutos. As indicações entre colchetes orientam a apresentação e não devem ser lidas.

## Integrante 1 — introdução, problema e motivação

Slides 1–5 | Tempo sugerido: 3 minutos, incluindo pausas.


### Slide 1 — apresentação

“Bom dia, pessoal. Nosso trabalho é sobre Isolation Forest, uma técnica de detecção de anomalias. Vamos explicar como ela funciona e apresentar uma aplicação em Python com transações fictícias de uma loja online.

A ideia principal é simples: observações que se diferenciam das demais tendem a ser mais fáceis de isolar. É isso que o algoritmo tenta medir.”

### Slide 2 — roteiro

“Primeiro, vamos apresentar o problema e a técnica. Depois, veremos o funcionamento, as aplicações e as limitações. Na parte prática, vamos explicar a preparação dos dados e discutir o que o modelo encontrou e o que deixou passar.”

### Slide 3 — o problema

“Detectar uma observação incomum não significa descobrir automaticamente um erro ou uma fraude. Uma compra pode ser rara e perfeitamente legítima.

Além disso, algumas situações só ficam estranhas quando combinamos as características. Por exemplo: uma compra de mil e cem reais pode ser comum para eletrônicos, mas esse mesmo valor por um único item de papelaria merece atenção.

[Apontar para o exemplo da loja.]

O problema também é que nem sempre temos registros classificados previamente como normais ou anormais. Precisamos de uma técnica que consiga procurar desvios sem depender desses exemplos.”

### Slide 4 — definição

“O Isolation Forest é um algoritmo não supervisionado, baseado em árvores aleatórias. Não supervisionado significa que ele não precisa receber os rótulos das anomalias durante o treinamento.

Ele divide os dados por meio de cortes e mede quantas divisões foram necessárias para separar cada observação. Uma observação que se separa rapidamente tende a receber uma pontuação de maior anormalidade.”

### Slide 5 — motivação

“A proposta foi explorar essa facilidade de isolamento. Em vez de calcular distâncias entre todas as observações, o método utiliza cortes aleatórios e pequenas subamostras.

Isso permite uma análise eficiente, embora o desempenho e o custo dependam dos parâmetros e dos dados utilizados. A técnica serve para priorizar casos que precisam de investigação.”

### Transição

“Agora que entendemos o problema e a ideia da técnica, vamos ver sua origem e como os cortes se transformam em uma pontuação.”

## Integrante 2 — histórico e funcionamento

Slides 6–9 | Tempo sugerido: 3 a 4 minutos, incluindo o diagrama.


### Slide 6 — histórico

“O Isolation Forest foi apresentado em 2008 por Liu, Ting e Zhou. Em 2012, os autores publicaram uma análise ampliada do método. Em 2016, ele passou a fazer parte do scikit-learn, facilitando seu uso em Python.

Depois surgiram variantes, como o Extended Isolation Forest, que permite trabalhar com cortes em outras direções.”

### Slide 7 — funcionamento

“Cada árvore começa com uma amostra dos registros. O algoritmo escolhe aleatoriamente uma característica e um valor de corte. Esse corte divide os dados em dois grupos, e o processo se repete.

[Apontar para o ponto laranja e a concentração de pontos.]

O ponto mais afastado pode ser separado dos demais com poucos cortes. Já os pontos próximos de muitas outras observações geralmente precisam de mais divisões.

Uma árvore sozinha pode produzir um resultado influenciado pelo acaso. Por isso usamos uma floresta: várias árvores, com diferentes cortes. O algoritmo combina os comprimentos dos caminhos para obter uma pontuação mais estável.

Na implementação, as árvores têm limite de profundidade. Quando uma folha ainda contém vários pontos, existe uma correção no cálculo do caminho.”

### Slide 8 — pontuação

“Na fórmula do artigo, o comprimento médio do caminho é normalizado pelo tamanho da subamostra. Caminhos mais curtos produzem pontuações maiores de anomalia.

[Apontar para as duas convenções do slide. Não é necessário ler a fórmula símbolo por símbolo.]

No scikit-learn, a função de decisão usa uma convenção diferente: valores negativos ficam abaixo do limiar e são sinalizados. Valores iguais ou maiores que zero não são sinalizados.

Essa pontuação não é uma probabilidade de fraude. Ela indica o quanto o registro é incomum segundo o modelo.”

### Slide 9 — código

“No nosso exemplo, criamos cem árvores e fixamos a semente em 42 para tornar a execução reproduzível.

O parâmetro contamination foi definido em cinco por cento antes da avaliação. Ele determina o limiar de triagem; não significa que sabemos que cinco por cento das compras são fraudes.

A função fit ajusta o modelo. A decision_function calcula os scores, e predict retorna menos um para candidata a anomalia e mais um para não sinalizada. A matriz X contém apenas as características preparadas, sem o gabarito.”

### Transição

“Com esse funcionamento em mente, vamos conhecer as aplicações e os cuidados necessários para usar a técnica.”

## Integrante 3 — aplicações, limitações e caso real

Slides 10–13 | Tempo sugerido: 3 minutos, incluindo pausas.


### Slide 10 — aplicações

“O Isolation Forest pode ser aplicado em diferentes contextos que precisam identificar observações incomuns.

Em finanças, pode ajudar na triagem de transações. Em segurança, pode sinalizar acessos ou tráfego fora do padrão. Na indústria, pode destacar leituras atípicas de sensores.

Também pode apoiar a conferência de registros de saúde, de vendas e de entregas. Em todos esses exemplos, o resultado funciona como um alerta para investigação, e não como uma decisão definitiva.”

### Slide 11 — limitações

“Apesar de ser simples de aplicar, a técnica tem limitações. Os cortes da versão tradicional são alinhados aos eixos, o que pode dificultar a representação de algumas relações entre características.

Ela também pode deixar passar anomalias locais: registros que são estranhos dentro de um grupo específico, mas não se destacam globalmente.

Antes do treinamento, precisamos tratar os valores ausentes e transformar as categorias em representações numéricas. A escolha do limiar também importa: mais alertas podem gerar mais trabalho e mais falsos positivos.

Por fim, o score indica que algo é incomum, mas não explica sozinho por que aquilo aconteceu.”

### Slide 12 — caso do cern

“Um caso documentado é o monitoramento da infraestrutura de nuvem do CERN, descrito em uma tese de 2022. O contexto do estudo envolvia aproximadamente quatorze mil máquinas virtuais.

O sistema utilizava Isolation Forest e dois modelos de autoencoder, combinando seus resultados para priorizar diariamente servidores incomuns.

A tese relata AUC-ROC acima de 0,95 para cada um dos três modelos na avaliação do estudo. Essa medida indica capacidade de distinguir os casos pelas pontuações; não equivale a dizer que o sistema acertou noventa e cinco por cento dos alertas.

Esse é um resultado específico daquela avaliação, que não pode ser transferido automaticamente para a nossa base.”

### Slide 13 — tendências

“As linhas de desenvolvimento incluem novas formas de fazer os cortes, novas representações dos dados, adaptações para dados que chegam continuamente e ferramentas para examinar os atributos dos alertas.

Outra possibilidade é combinar o Isolation Forest com outros modelos e com a revisão humana.”

### Transição

“Essas aplicações e limitações orientaram nosso estudo. Agora vamos apresentar os dados que criamos e as etapas da análise.”

## Integrante 4 — dados, preparação e resultados gerais

Slides 14–16 | Tempo sugerido: 3 a 4 minutos, incluindo o gráfico.


### Slide 14 — conjunto de dados

“Para a parte prática, criamos um CSV fictício com cento e vinte e seis transações de uma loja online, referentes a setembro de 2026.

Cada registro tem identificador e data, além de três características numéricas: valor, quantidade e percentual de desconto. As características categóricas são categoria do produto, país e forma de pagamento.

Incluímos quatro valores ausentes e seis casos documentados: três extremos, duas anomalias por combinação de características e uma compra indevida sem desvio observável. 

Essa distinção é importante: temos cinco anomalias observáveis. A compra indevida com atributos comuns é discutida separadamente, porque irregularidade não implica necessariamente anomalia estatística.”

### Slide 15 — preparação e modelo

“Primeiro, carregamos o CSV com Pandas e examinamos os tipos, as estatísticas e os valores ausentes.

Nos campos numéricos, preenchemos as ausências com a mediana da categoria, usando a mediana global como alternativa. Nos categóricos, usamos a moda, que é a categoria mais frequente. Essa escolha é simples, mas pode atribuir uma categoria incorreta.

Criamos o valor por item e a razão desse preço em relação à mediana da categoria. Assim conseguimos representar uma compra que tem valor comum globalmente, mas preço incompatível com o produto.

Também representamos a hora com seno e cosseno, para manter horários próximos, como vinte e três horas e meia-noite, próximos nessa representação.

As categorias foram codificadas com one-hot encoding, sem impor uma ordem entre elas. Depois aplicamos o Isolation Forest com cem árvores, contamination de cinco por cento e semente 42.

O gabarito só foi utilizado depois do ajuste, para avaliar os resultados.”

### Slide 16 — resultados

“[Apontar para o gráfico e os indicadores.]

Os pontos laranjas representam as compras sinalizadas. O eixo do valor usa escala logarítmica para permitir a visualização das compras menores junto ao valor extremo.

O modelo gerou sete alertas. Quatro correspondem às cinco anomalias observáveis, e três são falsos positivos. Isso representa precisão de aproximadamente cinquenta e sete por cento e recall de oitenta por cento.

A precisão mede quantos alertas estavam corretos; o recall mede quantas anomalias conhecidas foram encontradas. Como a base é sintética e foi usada no ajuste, esses números não demonstram desempenho em compras futuras.”

### Transição

“Agora vamos examinar o efeito do limiar e entender os casos encontrados e os que ficaram sem alerta.”

## Integrante 5 — interpretação e conclusão

Slides 17–20 | Tempo sugerido: 3 a 4 minutos, incluindo os casos.


### Slide 17 — limiar

“O histograma mostra a distribuição dos scores. Os registros à esquerda do zero são sinalizados como candidatos a anomalia.

Também comparamos diferentes frações de triagem, reutilizando os mesmos scores. Com três por cento, tivemos quatro alertas e três acertos. Com cinco por cento, foram sete alertas e quatro acertos.

Ao aumentar para dez por cento, passamos a treze alertas, mas continuamos com quatro acertos. Portanto, aumentar o número de alertas não garantiu encontrar mais anomalias nessa base: aumentou principalmente os falsos positivos.

Mantivemos cinco por cento como a análise principal, sem escolher o parâmetro pelo resultado do gabarito.”

### Slide 18 — casos

“O modelo encontrou quatro anomalias: T121, com valor de oito mil reais; T122, com quarenta e cinco itens; T123, com desconto de noventa e cinco por cento; e T124, com um item de papelaria a mil e cem reais.

O último caso mostra a importância da combinação de características. O valor não precisa ser o maior da base para ser incompatível com uma categoria.

T125, uma compra de eletrônicos baratos demais, não foi detectada. Esse é o falso negativo entre as cinco anomalias observáveis.

T126 também ficou sem alerta, mas tem outra interpretação: é uma compra indevida com atributos comuns. Ela está fora do cálculo do recall e demonstra que o algoritmo não identifica a intenção por trás da transação.

Os três falsos positivos são compras legítimas em Portugal com combinações relativamente raras. Isso não comprova que o país foi a causa dos alertas. Precisamos examinar produto, promoção e contexto antes de bloquear uma compra.”

### Slide 19 — referências

“Utilizamos os artigos originais, a documentação oficial do scikit-learn, o estudo do CERN e trabalhos sobre variantes do Isolation Forest. As referências estão disponíveis nos links do slide e na documentação do projeto.”

### Slide 20 — conclusão

“Nosso estudo mostrou que o Isolation Forest pode ajudar a priorizar observações incomuns. Em cento e vinte e seis transações, encontramos quatro das cinco anomalias observáveis, com três falsos positivos.

O aprendizado principal é que encontrar o incomum é apenas o início da investigação. Precisamos preparar os dados, calibrar o limiar e entender o contexto.

Para uma aplicação real, o próximo passo seria avaliar dados históricos e compras futuras, além de revisar os alertas com quem conhece o negócio.

Obrigado. Estamos disponíveis para perguntas.”
