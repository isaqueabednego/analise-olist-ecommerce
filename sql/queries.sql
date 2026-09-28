-- ============================================================
-- Queries de Análise - E-commerce Olist
-- ============================================================

-- 1. Faturamento por mês
SELECT strftime('%Y-%m', order_purchase_timestamp) AS mes,
       SUM(valor_item) AS faturamento
FROM fato_pedidos
GROUP BY mes
ORDER BY mes;

-- 2. Top 10 categorias por faturamento
SELECT p.product_category_name,
       SUM(f.valor_item) AS faturamento
FROM fato_pedidos f
JOIN dim_produtos p ON f.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY faturamento DESC
LIMIT 10;

-- 3. Ranking de vendedores por nota média (sem inflar peso de pedidos com mais itens)
SELECT seller_id, AVG(review_score) AS nota_media,
       RANK() OVER (ORDER BY AVG(review_score) DESC) AS ranking
FROM (
    SELECT DISTINCT order_id, seller_id, review_score
    FROM fato_pedidos
)
GROUP BY seller_id
ORDER BY nota_media DESC;