# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Install the dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire application and migrations into the container
COPY . /code

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run migrations, run seeding and start the FastAPI application using uvicorn
CMD ["sh", "-c", "alembic upgrade head && python seed.py && fastapi run main.py --port 8000"]