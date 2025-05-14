import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Crear un DataFrame con datos desde el año 2022 por mes
fechas = pd.date_range(start='2022-01-01', end='2024-12-31', freq='MS')
data = pd.DataFrame({
    'fecha': fechas,
    'agente': np.random.choice(['Agente A', 'Agente B', 'Agente C', 'Agente D'], size=len(fechas)),
    'producto': np.random.choice(['Producto X', 'Producto Y', 'Producto Z'], size=len(fechas)),
    'ventas': np.random.randint(100, 1000, size=len(fechas)),
    'comision': np.random.randint(10, 100, size=len(fechas))
})

# Aumentar el tamaño del DataFrame duplicando los datos
data = pd.concat([data]*10, ignore_index=True)

# Guardar el DataFrame en un archivo CSV
data.to_csv('C:\proyecto\datos_comisiones_ml.csv', index=False)

# Cargar los datos desde el archivo CSV
data = pd.read_csv('C:\proyecto\datos_comisiones_ml.csv')

# Convertir la columna 'fecha' a un formato numérico (año y mes)
data['año'] = pd.to_datetime(data['fecha']).dt.year
data['mes'] = pd.to_datetime(data['fecha']).dt.month

# Separar las características (X) y la variable objetivo (y)
X = data[['agente', 'producto', 'ventas', 'año', 'mes']]
y = data['comision']

# Crear un transformador para codificar las variables categóricas
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['agente', 'producto', 'año', 'mes'])
    ],
    remainder='passthrough'
)

# Crear el modelo de regresión lineal dentro de un pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Crear un DataFrame con las fechas del año 2025 para hacer predicciones futuras
fechas_2025 = pd.date_range(start='2025-01-01', end='2025-12-31', freq='MS')
future_data = pd.DataFrame({
    'fecha': fechas_2025,
    'agente': np.random.choice(['Agente A', 'Agente B', 'Agente C', 'Agente D'], size=len(fechas_2025)),
    'producto': np.random.choice(['Producto X', 'Producto Y', 'Producto Z'], size=len(fechas_2025)),
    'ventas': np.random.randint(100, 1000, size=len(fechas_2025))
})

# Convertir la columna 'fecha' a un formato numérico (año y mes) en los datos futuros
future_data['año'] = pd.to_datetime(future_data['fecha']).dt.year
future_data['mes'] = pd.to_datetime(future_data['fecha']).dt.month

# Hacer predicciones futuras para el año 2025
future_predictions = model.predict(future_data[['agente', 'producto', 'ventas', 'año', 'mes']])

# Crear un DataFrame con las predicciones futuras
predictions_df = pd.DataFrame({
    'fecha': future_data['fecha'],
    'agente': future_data['agente'],
    'producto': future_data['producto'],
    'ventas': future_data['ventas'],
    'comision_predicha': future_predictions
})



print("Las predicciones futuras para el año 2025 se han guardado en 'Descargas/predicciones_futuras_2025.xlsx'.")

# Agrupar las predicciones por producto y calcular el total de ventas predichas
ventas_futuras_por_producto = future_data.groupby('producto')['ventas'].sum().reset_index()

# Ordenar los productos por ventas predichas en orden descendente
ventas_futuras_por_producto = ventas_futuras_por_producto.sort_values(by='ventas', ascending=False)

# Agrupar las predicciones por agente y calcular el total de ventas predichas
ventas_futuras_por_agente = future_data.groupby('agente')['ventas'].sum().reset_index()

# Ordenar los agentes por ventas predichas en orden descendente
ventas_futuras_por_agente = ventas_futuras_por_agente.sort_values(by='ventas', ascending=False)

# Agrupar las predicciones por agente y calcular el total de comisiones predichas
comisiones_por_agente = predictions_df.groupby('agente')['comision_predicha'].sum().reset_index()

