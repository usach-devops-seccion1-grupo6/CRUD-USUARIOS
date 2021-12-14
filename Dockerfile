FROM python:3.9-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN /opt/venv/bin/python -m pip install --upgrade pip
RUN /opt/venv/bin/python -m pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

# Make Entrypoint executable
COPY .env.dist .env
RUN chmod +x /app/docker-entrypoint.sh


# Run the app when the container launches
ENTRYPOINT ["/app/docker-entrypoint.sh"]
