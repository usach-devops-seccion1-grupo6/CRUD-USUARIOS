# Use an official Python runtime as a parent image
FROM python:3.7-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000


# Make Entrypoint executable
RUN chmod +x /app/docker-entrypoint.sh


# Run the app when the container launches
ENTRYPOINT ["/app/docker-entrypoint.sh"]
