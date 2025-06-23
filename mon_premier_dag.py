# airflow-dataops-cours/dags/mon_premier_dag.py
from __future__ import annotations

import pendulum # Librairie pour gérer les dates et heures

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="mon_premier_dag_v1", # Identifiant unique de votre DAG
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"), # Date de début (dans le passé)
    catchup=False, # Ne pas essayer de rattraper les exécutions passées
    schedule=None, # Pas de planification automatique, déclenchement manuel
    tags=["test", "cours_dataops"], # Pour organiser/filtrer les DAGs dans l'UI
) as dag:
    tache_hello_airflow = BashOperator(
        task_id="dire_bonjour_airflow", # Identifiant unique de la tâche
        bash_command='echo "Bonjour Airflow, je fonctionne dans Docker ! 🎉 Date: $(date)"',
    )
