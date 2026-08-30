USE datamining_ex06;

DELIMITER //

CREATE PROCEDURE preencher_clientes()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 30 DO
        INSERT INTO clientes_original
        VALUES (
            CONCAT('C', LPAD(i, 3, '0')),
            CONCAT('Cliente ', LPAD(i, 3, '0')),
            20 + MOD(i, 16),
            CASE MOD(i - 1, 5)
                WHEN 0 THEN 'Sao Paulo'
                WHEN 1 THEN 'Campinas'
                WHEN 2 THEN 'Santos'
                WHEN 3 THEN 'Rio de Janeiro'
                ELSE 'Niteroi'
            END,
            CASE MOD(i - 1, 5)
                WHEN 0 THEN 'SP'
                WHEN 1 THEN 'SP'
                WHEN 2 THEN 'SP'
                WHEN 3 THEN 'RJ'
                ELSE 'RJ'
            END,
            2200 + (i * 180)
        );
        SET i = i + 1;
    END WHILE;
END//

CREATE PROCEDURE preencher_produtos()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
        INSERT INTO produtos_original
        VALUES (
            CONCAT('P', LPAD(i, 3, '0')),
            CASE MOD(i - 1, 5)
                WHEN 0 THEN 'Notebook'
                WHEN 1 THEN 'Mouse'
                WHEN 2 THEN 'Teclado'
                WHEN 3 THEN 'Monitor'
                ELSE 'Fone Bluetooth'
            END,
            CASE MOD(i - 1, 5)
                WHEN 0 THEN 'Informatica'
                WHEN 1 THEN 'Acessorios'
                WHEN 2 THEN 'Acessorios'
                WHEN 3 THEN 'Informatica'
                ELSE 'Audio'
            END,
            100 + (i * 50)
        );
        SET i = i + 1;
    END WHILE;
END//

CREATE PROCEDURE preencher_vendas()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE quantidade_atual INT;
    DECLARE preco_atual DECIMAL(10,2);
    SET quantidade_atual = 1;
    SET preco_atual = 100;
    WHILE i <= 100 DO
        SET quantidade_atual = 1 + MOD(i, 5);
        SET preco_atual = 100 + ((1 + MOD(i - 1, 10)) * 50);
        INSERT INTO vendas_original
        VALUES (
            CONCAT('V', LPAD(i, 3, '0')),
            DATE_ADD('2026-01-01', INTERVAL (i - 1) DAY),
            CONCAT('C', LPAD(1 + MOD(i - 1, 30), 3, '0')),
            CONCAT('P', LPAD(1 + MOD(i - 1, 10), 3, '0')),
            quantidade_atual,
            preco_atual,
            quantidade_atual * preco_atual
        );
        SET i = i + 1;
    END WHILE;
END//

DELIMITER ;

CALL preencher_clientes();
CALL preencher_produtos();
CALL preencher_vendas();

DROP PROCEDURE preencher_clientes;
DROP PROCEDURE preencher_produtos;
DROP PROCEDURE preencher_vendas;

CREATE TABLE clientes_problematicos AS SELECT * FROM clientes_original;
CREATE TABLE produtos_problematicos AS SELECT * FROM produtos_original;
CREATE TABLE vendas_problematicas AS SELECT * FROM vendas_original;

ALTER TABLE clientes_problematicos
    MODIFY estado CHAR(2) NULL,
    MODIFY renda DECIMAL(10,2) NULL;
ALTER TABLE produtos_problematicos
    MODIFY valor_unitario DECIMAL(10,2) NULL;
ALTER TABLE vendas_problematicas
    MODIFY id_cliente VARCHAR(4) NULL,
    MODIFY quantidade INT NULL,
    MODIFY valor_total DECIMAL(10,2) NULL;

UPDATE clientes_problematicos SET renda = NULL WHERE id_cliente = 'C010';
UPDATE clientes_problematicos SET estado = 'XX' WHERE id_cliente = 'C005';
INSERT INTO clientes_problematicos
    SELECT * FROM clientes_original WHERE id_cliente = 'C015';

UPDATE produtos_problematicos SET valor_unitario = NULL WHERE id_produto = 'P005';
UPDATE produtos_problematicos SET valor_unitario = -50 WHERE id_produto = 'P003';

UPDATE vendas_problematicas SET quantidade = NULL WHERE id_venda = 'V020';
UPDATE vendas_problematicas SET quantidade = -2 WHERE id_venda = 'V050';
UPDATE vendas_problematicas SET valor_total = 9999 WHERE id_venda = 'V030';
UPDATE vendas_problematicas SET id_cliente = 'C999' WHERE id_venda = 'V040';
INSERT INTO vendas_problematicas
    SELECT * FROM vendas_original WHERE id_venda = 'V010';

CREATE OR REPLACE VIEW vendas_problematicas_completas AS
SELECT
    v.id_venda,
    v.data_venda,
    v.id_cliente,
    c.nome_cliente,
    c.estado AS estado_cliente,
    v.id_produto,
    p.nome_produto,
    p.categoria,
    v.quantidade,
    v.valor_unitario,
    v.valor_total
FROM vendas_problematicas AS v
LEFT JOIN clientes_problematicos AS c ON c.id_cliente = v.id_cliente
LEFT JOIN produtos_problematicos AS p ON p.id_produto = v.id_produto;
