# Use official Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy local files to container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port used by Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app1.py", "--server.port=8501", "--server.address=0.0.0.0"]

