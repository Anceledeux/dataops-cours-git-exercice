# hello.py
import os
import pandas # Just to show dependency installation

message = "Hello DataOps from Docker!"
print(message)

# Petite démonstration que les fichiers sont bien dans le conteneur
print("\nContenu du répertoire de travail (/app) dans le conteneur :")
try:
    for item in os.listdir("."): # Le WORKDIR est /app
        print(f"- {item}")
except Exception as e:
    print(f"Erreur lors du listage des fichiers : {e}")

print(f"\nVersion de pandas installée : {pandas.__version__}")