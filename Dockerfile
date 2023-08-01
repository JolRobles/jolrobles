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
# Comando para ejecutar tu aplicación Django

# The error message "app did not turn healthy after several checksundefined" suggests that the Docker healthcheck is failing.

# To fix this, we need to add a HEALTH toCHECK instruction the Dockerfile.

# Add a healthcheck to ensure that the container is healthy

HEALTHCHECK --interval=5s --timeout=5s \

CMD curl -f http://localhost:8000/ || exit 1

# The healthcheck command performs an HTTP GET request to the localhost on port 8000 every 5 seconds.

# If the response status code is not 2xx, the healthcheck will fail and the container will be considered unhealthy.

# This ensures that the application is running properly before considering it healthy.
