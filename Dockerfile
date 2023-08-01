# Usa la imagen oficial de Python como base
FROM python:3.9.2

# Establece variables de entorno (si es necesario)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /jolrobles

# Instala las dependencias
COPY requirements.txt /jolrobles/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu proyecto Django al contenedor
COPY . /jolrobles/

# Expone el puerto en el que se ejecutará tu aplicación Django (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar tu aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
