import pandas as pd
import os

def transform_data_function(source_data_path: str, target_data_path: str):
    """
    Lit les données propres, les transforme, et sauvegarde le résultat.
    Cette fonction sera appelée par le PythonOperator d'Airflow.
    """
    print(f"--- Transformation : Lecture depuis {source_data_path} ---")
    try:
        df = pd.read_csv(source_data_path)
    except FileNotFoundError:
        print(f"ERREUR : Le fichier d'entrée n'a pas été trouvé à l'emplacement {source_data_path}")
        raise
    
    # La même logique de transformation qu'avant
    df['montant_total_ht'] = df['quantite'] * df['prix_unitaire_ht']
    ventes_aggregees = df.groupby(['id_produit', 'nom_produit']).agg(
        quantite_totale=('quantite', 'sum'),
        montant_total_ventes_ht=('montant_total_ht', 'sum')
    ).reset_index()

    print(f"Données agrégées. Nombre de produits uniques : {len(ventes_aggregees)}")
    # Crée le dossier de destination s'il n'existe pas
    os.makedirs(os.path.dirname(target_data_path), exist_ok=True)
    
    #Sauvegarde du fichier final 
    ventes_aggregees.to_csv(target_data_path, index=False)
    print(f"--- Transformation terminée, fichier sauvegardé dans {target_data_path} ---")