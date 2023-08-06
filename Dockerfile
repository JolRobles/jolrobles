
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
# The previous healthcheck command was incorrect and triggered the " not turnapp healthy did after several checks" error
# To fix this, we need to use a valid healthcheck command
HEALTHCHECK --interval=5s --timeout=5s \
  CMD curl -f http://localhost:8000/ || exit 1
