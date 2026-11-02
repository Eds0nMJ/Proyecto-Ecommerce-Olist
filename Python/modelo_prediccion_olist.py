import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

servidor = r'localhost\SQLEXPRESS'
base_datos = 'Portafolio_Olist'
cadena_conexion = f"DRIVER={{SQL Server}};SERVER={servidor};DATABASE={base_datos};Trusted_Connection=yes;"

try:
    print("Conectando a la base de datos...")
    # Usamos un bloque with para manejar el warning de SQLAlchemy a futuro
    import warnings
    warnings.filterwarnings('ignore') # Oculta los warnings visuales en la consola
    
    conexion = pyodbc.connect(cadena_conexion)
    print("¡Conexión exitosa a SQL Server!\n")

    query = """
    SELECT 
        Anio, Mes,
        DATEFROMPARTS(Anio, Mes, 1) AS Periodo_Mensual,
        ROUND(SUM(Precio_Real), 2) AS Ingresos_Totales
    FROM vw_Ventas_Ecommerce
    GROUP BY Anio, Mes
    ORDER BY Anio, Mes;
    """

    # Extraer y preparar el DataFrame
    df_ventas = pd.read_sql(query, conexion)
    # Forma actualizada sin inplace=True para evitar el warning
    df_ventas['Periodo_Mensual'] = pd.to_datetime(df_ventas['Periodo_Mensual'])
    df_ventas = df_ventas.set_index('Periodo_Mensual')

    print("--- Datos Históricos (Últimos 5 meses) ---")
    print(df_ventas.tail())

    # ---------------------------------------------------------
    # MOTOR PREDICTIVO (Regresión Lineal)
    # ---------------------------------------------------------
    # Creamos un índice numérico de tiempo (0, 1, 2, 3...) para que el modelo lo entienda
    df_ventas['Indice_Tiempo'] = np.arange(len(df_ventas))
    
    X = df_ventas[['Indice_Tiempo']]
    y = df_ventas['Ingresos_Totales']

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Proyectar los próximos 3 meses
    meses_futuros = np.array([
        [len(df_ventas)], 
        [len(df_ventas) + 1], 
        [len(df_ventas) + 2]
    ])
    predicciones = modelo.predict(meses_futuros)

    print("\n--- Proyección de Ingresos (Próximos 3 meses) ---")
    for i, pred in enumerate(predicciones):
        print(f"Mes {i+1} proyectado: R$ {pred:,.2f}")

    # ---------------------------------------------------------
    # VISUALIZACIÓN
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(df_ventas.index, df_ventas['Ingresos_Totales'], marker='o', linestyle='-', color='#004C99', label='Ingresos Históricos')
    plt.title('Tendencia de Ingresos Mensuales - Olist E-commerce', fontsize=14)
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos (R$)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    print("\nGenerando gráfico... (Cierra la ventana del gráfico para finalizar el programa)")
    plt.show()

except Exception as e:
    print("\nOcurrió un error:")
    print(e)

finally:
    if 'conexion' in locals():
        conexion.close()
        print("\nConexión a SQL Server cerrada.")