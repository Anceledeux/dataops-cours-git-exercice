# airflow-dataops-cours/dags/dag_avec_dependances.py
from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# Définition du DAG
with DAG(
    dag_id="dag_avec_dependances_v1",
    start_date=pendulum.today("UTC").subtract(days=1),
    catchup=False,
    schedule=None,
    tags=["exercice", "dépendances"],
    doc_md="""
    ### DAG avec Dépendances
    
    Ce DAG simple démontre comment créer une dépendance entre deux tâches.
    - `premiere_etape` s'exécute en premier.
    - `deuxieme_etape` s'exécute seulement après la réussite de la première.
    """,
) as dag:
    # Tâche 1: Simule une première étape qui prend un peu de temps
    tache_1 = BashOperator(
        task_id="premiere_etape",
        # La commande echo affiche un message, et `sleep 5` met la tâche en pause pendant 5 secondes
        # pour que nous puissions bien observer l'enchaînement dans l'UI.
        bash_command='echo "Étape 1 : Préparation des données en cours..." && sleep 5',
    )

    # Tâche 2: Simule une deuxième étape
    tache_2 = BashOperator(
        task_id="deuxieme_etape",
        bash_command='echo "Étape 2 : Traitement terminé avec succès !"',
    )

    # Définition de la dépendance entre les tâches
    # La tâche 1 DOIT se terminer avec succès AVANT que la tâche 2 ne commence.
    tache_1 >> tache_2