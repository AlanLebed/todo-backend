# Usa una imagen base oficial de Python
FROM python:3.12.3-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente de la aplicación en el contenedor
COPY . .

# Expone el puerto que Flask utilizará
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
