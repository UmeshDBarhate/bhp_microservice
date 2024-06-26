#DockerFile

# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /bhp_microservice

# Copy the current directory contents into the container at /app
COPY . /bhp_microservice

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8001

# Run manage.py to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]


