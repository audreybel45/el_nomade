# Usar una imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar el archivo de requisitos y el código
COPY requirements.txt /code/
COPY . /code/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
