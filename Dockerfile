FROM python:3.11-slim

# Install light core media packages
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg curl git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Pull project structure over to the container node
COPY . .

# Install your tiny Python packages safely with no space overflow risks
RUN pip install --no-cache-dir streamlit google-genai

# Expose Render standard web container port
EXPOSE 10000

# Tell Docker to run your brand new Streamlit UI dashboard
CMD ["streamlit", "run", "dashboard.py", "--server.port", "10000", "--server.address", "0.0.0.0"]
