USE Portafolio_Olist;
GO

CREATE OR ALTER VIEW vw_Ventas_Ecommerce AS
SELECT 
    o.order_id,
    -- Extraemos la fecha en formato limpio (YYYY-MM-DD)
    CAST(o.order_purchase_timestamp AS DATE) AS Fecha_Compra,
    -- Sacamos el Año y Mes directo para las gráficas de Power BI y el pronóstico en Python
    YEAR(o.order_purchase_timestamp) AS Anio,
    MONTH(o.order_purchase_timestamp) AS Mes,
    -- Arreglamos el problema de los decimales dividiendo entre 100 (usamos .0 para forzar decimales)
    CAST(oi.price AS FLOAT) / 100.0 AS Precio_Real,
    CAST(oi.freight_value AS FLOAT) / 100.0 AS Costo_Envio_Real,
    p.product_category_name AS Categoria_Producto,
    c.customer_state AS Estado_Cliente,
    c.customer_city AS Ciudad_Cliente
FROM olist_orders_dataset o
INNER JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
INNER JOIN olist_products_dataset p ON oi.product_id = p.product_id
INNER JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
-- REGLA DE NEGOCIO: Solo tomamos en cuenta pedidos completados (entregados)
WHERE o.order_status = 'delivered';
GO

SELECT TOP 15 * FROM vw_Ventas_Ecommerce;