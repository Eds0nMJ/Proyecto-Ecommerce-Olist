USE Portafolio_Olist;
GO

SELECT 
    Anio,
    Mes,
    -- Generamos una fecha base (el primer día de cada mes) que es un requisito estricto para los modelos de Series de Tiempo en Python y Power BI
    DATEFROMPARTS(Anio, Mes, 1) AS Periodo_Mensual,
    COUNT(DISTINCT order_id) AS Total_Pedidos,
    ROUND(SUM(Precio_Real), 2) AS Ingresos_Totales,
    ROUND(SUM(Precio_Real) / COUNT(DISTINCT order_id), 2) AS Ticket_Promedio
FROM vw_Ventas_Ecommerce
GROUP BY Anio, Mes
ORDER BY Anio, Mes;