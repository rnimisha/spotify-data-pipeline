FROM apache/airflow:2.7.3

# Set the working directory
WORKDIR /opt/airflow

# Set the PYTHONPATH to include the required directories
ENV PYTHONPATH "/opt/scripts:/opt/data:/opt/config"

# Copy your scripts, data, and requirements.txt into the container
COPY scripts/ /opt/scripts/
COPY data/ /opt/data/
COPY config/ /opt/config/
COPY .env /opt/.env
COPY .spotify_cache /opt/.spotify_cache
COPY .spotify_cache /opt/scripts/utils/.spotify_cache
COPY requirements.txt /opt/requirements.txt  

# Change ownership of .spotify_cache to airflow user
USER root
RUN chown -R airflow:root /opt/.spotify_cache

# Grant read and write permissions to the airflow group
RUN chmod -R 775 /opt/.spotify_cache

# Switch back to the airflow user for further operations
USER airflow

# Install requirements
RUN pip install --no-cache-dir -r /opt/requirements.txt
