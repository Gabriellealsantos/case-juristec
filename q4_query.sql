-- q4_query.sql

SELECT 
    c.nome, 
    p.assunto, 
    p.data_abertura
FROM 
    clientes c
INNER JOIN 
    processos p ON c.id_cliente = p.id_cliente
WHERE 
    c.estado = 'SP'
    AND p.data_abertura >= '2023-01-01' 
    AND p.data_abertura <= '2023-12-31';
