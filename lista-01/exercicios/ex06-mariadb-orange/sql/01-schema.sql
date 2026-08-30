USE datamining_ex06;

DROP VIEW IF EXISTS vendas_problematicas_completas;
DROP TABLE IF EXISTS vendas_problematicas;
DROP TABLE IF EXISTS produtos_problematicos;
DROP TABLE IF EXISTS clientes_problematicos;
DROP TABLE IF EXISTS vendas_original;
DROP TABLE IF EXISTS produtos_original;
DROP TABLE IF EXISTS clientes_original;

CREATE TABLE clientes_original (
    id_cliente VARCHAR(4) NOT NULL,
    nome_cliente VARCHAR(80) NOT NULL,
    idade INT NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    renda DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_cliente)
);

CREATE TABLE produtos_original (
    id_produto VARCHAR(4) NOT NULL,
    nome_produto VARCHAR(80) NOT NULL,
    categoria VARCHAR(40) NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_produto)
);

CREATE TABLE vendas_original (
    id_venda VARCHAR(4) NOT NULL,
    data_venda DATE NOT NULL,
    id_cliente VARCHAR(4) NOT NULL,
    id_produto VARCHAR(4) NOT NULL,
    quantidade INT NOT NULL,
    valor_unitario DECIMAL(10,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_venda)
);
