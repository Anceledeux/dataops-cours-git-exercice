import pandas as pd
import os

def validate_data_function(source_data_path: str, target_data_path: str):
    """
    Lit un CSV, le nettoie, et le sauvegarde.
    Cette fonction sera appelée par le PythonOperator d'Airflow.
    """
    print(f"--- Validation : Lecture depuis {source_data_path} ---")
    df = pd.read_csv(source_data_path)
    
    # Logique de nettoyage
    df.dropna(subset=['id_transaction'], inplace=True)
    df.drop_duplicates(subset=['id_transaction'], inplace=True, keep='first')
    df['quantite'] = pd.to_numeric(df['quantite'], errors='coerce')
    df.dropna(subset=['quantite'], inplace=True)
    df['quantite'] = df['quantite'].astype(int)
    df = df[df['quantite'] > 0]
    df['prix_unitaire_ht'] = pd.to_numeric(df['prix_unitaire_ht'], errors='coerce')
    df.dropna(subset=['prix_unitaire_ht'], inplace=True)
    df = df[df['prix_unitaire_ht'] > 0]
    df.dropna(subset=['nom_produit'], inplace=True)
    df['nom_produit'] = df['nom_produit'].str.strip().str.title()

    print(f"Lignes après validation : {len(df)}")
    
    #On crée le dossier s'il n'existe pas 
    os.makedirs(os.path.dirname(target_data_path), exist_ok=True)
    #Sauvegarde du dataframe nettoyé
    df.to_csv(target_data_path, index=False)
    print(f"--- Validation terminée, fichier sauvegardé dans {target_data_path} ---")