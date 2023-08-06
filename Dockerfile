# Use the official Python image as the base
FROM python:3.9.2

# Set environment variables (if necessary)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /jlrobles

# Install dependencies
COPY requirements.txt /jlrobles/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project code to the container
COPY . /jlrobles/

# Expose the port on which your Django application will run (e.g., 8000)
EXPOSE 8000

# Command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Add a healthcheck to ensure container is healthy
HEALTHCHECK --interval=5s --timeout=5s \
  CMD curl -f http://localhost:8000/ || exit 1

# The error message "app did not turn healthy after several checks"undefined suggests that the Docker healthcheck is failing.
# To fix this, we need to add a HEALTHCHECK instruction to the Dockerfile.
# The healthcheck command performs an HTTP GET request to the localhost on port 8000 every 5 seconds.
# If the response status code is not 2xx, the healthcheck will fail and the container will be unhealthy considered.
# This ensures that the application is running properly before considering it healthy.
