# Utiliza una imagen base de Python oficial
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu script de Streamlit
COPY app.py .

# Expone el puerto que usa Streamlit
EXPOSE 8501

# Comando para iniciar la aplicación Streamlit
CMD ["streamlit", "run", "app.py"]
