# Dockerfile
# On part de l'image officielle d'Airflow
FROM apache/airflow:2.9.2

# On passe en utilisateur root temporairement pour installer des choses
USER root
# On crée le dossier qui recevra nos données, et on donne les permissions
# à l'utilisateur 'airflow' qui exécutera les tâches.
RUN mkdir -p /opt/airflow/data/processing /opt/airflow/data/output && \
    chown -R airflow:root /opt/airflow/data
USER airflow

# On copie nos scripts de transformation dans l'image
COPY ./scripts_pipeline /opt/airflow/scripts_pipeline

# On installe les librairies Python dont nos scripts ont besoin (ici, pandas)
RUN pip install --no-cache-dir pandas==2.2.2