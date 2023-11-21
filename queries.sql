-- SQLite
-- para rodar, precisa usar o comando Ctrl+shift+q


SELECT name AS nome, age AS idade, id
--SELECT name, age, id - seleciona só os que eu quero

FROM tabela
-- FROM [nome da tabela]
-- usando AS para mudar o nome da tabela,
--pode chamar depois com o nome escolhido

WHERE nome = 'Juliana'
WHERE idade BETWEEN 10 AND 15
-- seleciona o intervalo escolhido para exibição

DELETE FROM tabela
WHERE name = 'Barbie'
-- deletar linhas

SELECT *
FROM tabela
-- SELECT * - pega tudo 

ALTER TABLE tabela 
DROP COLUMN age
-- dropar coluna

DROP TABLE tabela
-- dropar a tabela