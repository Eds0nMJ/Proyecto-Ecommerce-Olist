# 📊 Proyecto de Análisis de Datos: E-commerce Olist

Pipeline analítico de punta a punta desarrollado para portafolio profesional, integrando bases de datos relacionales, modelado predictivo en Python y visualización ejecutiva en Power BI.

---

## 🛠️ Tecnologías y Herramientas Utilizadas
* **SQL Server / SSMS:** Almacenamiento, limpieza de datos, manejo de nulos y creación de vistas analíticas optimizadas (`vw_Ventas_Ecommerce`).
* **Python (Pandas, Scikit-Learn, Pyodbc):** Extracción vía pipeline corporativo y desarrollo de un modelo de Machine Learning (Regresión Lineal) para *Forecasting* de ingresos.
* **Power BI Desktop:** Modelado dimensional en Esquema de Estrella, creación de Tabla Calendario, métricas DAX avanzadas de Inteligencia de Tiempo (`% Crecimiento MoM`) y diseño de Dashboard Ejecutivo.

---

## 📂 Estructura del Repositorio
- `sql/`: Scripts de consultas, creación de base de datos y vistas analíticas.
- `python/`: Script de conexión a base de datos y modelo predictivo de series temporales.
- `dashboard/`: Archivo fuente del reporte interactivo en Power BI (`.pbix`).
- `assets/`: Capturas de pantalla del tablero final.

---

## 📈 Resumen del Proyecto y Resultados
1. **Fase SQL:** Se procesaron más de 100,000 registros de transacciones de comercio electrónico en Brasil, uniendo tablas de pedidos, ítems y productos para filtrar anomalías y estructurar una base limpia.
2. **Fase Python:** Se conectó la base de datos de forma segura mediante `pyodbc` para extraer métricas agregadas mensuales, proyectando con éxito la tendencia de crecimiento de ingresos de Olist para los próximos trimestres.
3. **Fase Power BI:** Se construyó un tablero gerencial interactivo que incluye:
   - Tarjetas de indicadores clave (**Total de Ingresos** y **Ticket Promedio**).
   - Gráfico de tendencia temporal continua por año y mes.
   - Segmentadores dinámicos por año y categoría de producto.
   - Análisis geográfico del impacto de ventas por estado en Brasil.

---
*Desarrollado por Edson Bartolo Huere - Estudiante de Computación Científica (UNMSM)*
