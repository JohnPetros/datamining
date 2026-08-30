# Respostas — Exercício 6

## a) Quais problemas foram encontrados?

Foram encontrados dados vazios, valores inválidos, duplicidades,
inconsistências nos valores das vendas e uma referência a cliente inexistente.

## b) Em quais campos eles apareceram?

- `clientes_problematicos.estado`: estado inválido `XX`;
- `clientes_problematicos.renda`: valor ausente;
- `clientes_problematicos.id_cliente`: cliente duplicado;
- `produtos_problematicos.valor_unitario`: valor ausente e valor negativo;
- `vendas_problematicas.id_venda`: venda duplicada;
- `vendas_problematicas.quantidade`: valor ausente e valor negativo;
- `vendas_problematicas.valor_total`: total inconsistente com quantidade vezes valor unitário;
- `vendas_problematicas.id_cliente`: referência ao cliente inexistente `C999`.

## c) Quantos registros foram afetados?

Considerando as linhas físicas das tabelas problemáticas:

- clientes: 4 linhas;
- produtos: 2 linhas;
- vendas: 6 linhas;
- total: **12 linhas afetadas**.

Há **10 identificadores distintos** afetados, porque `C015` e `V010` aparecem
duplicados.

## d) O fato de os dados estarem armazenados em um banco de dados garante que estejam corretos?

Não. O banco de dados organiza e armazena as informações, mas não garante que
elas estejam corretas. Para isso, é necessário configurar regras de validação,
restrições, chaves estrangeiras, valores obrigatórios e processos de revisão
ou limpeza dos dados.
