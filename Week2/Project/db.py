# importe le module qui permet d’accéder aux variables d’environnement (comme DATABASE_URL).
import os
# permet de charger automatiquement les variables contenues dans le fichier .env.
from dotenv import load_dotenv
# importe la librairie PostgreSQL pour Python.
import psycopg

# charge le fichier `.env` pour pouvoir utiliser DATABASE_URL
load_dotenv()
# récupère la valeur de la variable d'environnement DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Ouvre une connexion simple à PostgreSQL
def get_connection():
    return psycopg.connect(DATABASE_URL) 


