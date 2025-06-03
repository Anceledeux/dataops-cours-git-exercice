# mon-web-docker/web_server.py
import http.server
import socketserver
import os

PORT = 8000
# Le serveur servira les fichiers depuis le sous-dossier 'html_files'
# par rapport à l'emplacement du script web_server.py dans le conteneur.
WEB_DIR = os.path.join(os.path.dirname(__file__), 'html_files')

# Change le répertoire courant vers le dossier web_dir pour que SimpleHTTPRequestHandler serve depuis là
try:
    os.chdir(WEB_DIR)
except FileNotFoundError:
    print(f"ERREUR: Le dossier '{WEB_DIR}' n'a pas été trouvé. Assurez-vous qu'il existe et contient index.html.")
    exit(1)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serveur démarré sur http://0.0.0.0:{PORT}")
    print(f"Sert les fichiers depuis le répertoire : {os.getcwd()}") # Affiche le répertoire servi
    print(f"Pour accéder depuis l'extérieur du conteneur, utilisez le port mappé sur votre hôte (ex: http://localhost:8888).")
    httpd.serve_forever()