USE Portafolio_Olist;
GO

-- Consulta de validación y unión base (Join de Pedidos con Ítems y Productos)
SELECT TOP 10 
    o.order_id,
    o.order_purchase_timestamp,
    oi.price,
    oi.freight_value,
    p.product_category_name
FROM olist_orders_dataset o
INNER JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
INNER JOIN olist_products_dataset p ON oi.product_id = p.product_id;