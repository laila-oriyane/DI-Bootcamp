from deep_translator import GoogleTranslator
import os
import platform
# Importe la fonction `get_connection()` du fichier `db.py` pour exécuter les requêtes SQL.
from db import get_connection
# Importe la classe qui permet de traduire du texte.
from translate import Translator
# Importe la classe google text to speech qui permet de générer des fichiers audio à partir de texte .mp3
from gtts import gTTS

class Blog:
    # Fonction appelée quand on crée un objet Blog. `id=None` car le blog n’a pas encore de numéro dans la base avant l’enregistrement.
    def __init__(self, id=None, title=None, content=None, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.content = content 
        self.created_at = created_at
        self.updated_at = updated_at

    # Convertir un objet Blog → dictionnaire JSON
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }

    # Enregistrer un nouveau blog dans la base PostgreSQL.
    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO blogs (title, content)
            VALUES (%s, %s)
            RETURNING id, created_at, updated_at
            """,
            (self.title, self.content)
        )
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        self.id,self.created_at,self.updated_at = result
        return self
    
    # Update blog
    def update(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE blogs SET title=%s, content=%s, updated_at=NOW()
            WHERE id=%s
            RETURNING updated_at
            """,
            (self.title, self.content, self.id)
        )

        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        self.updated_at = result[0]
        return self
    
    # Delete blog
    def delete(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM blogs WHERE id=%s", (self.id,))
        conn.commit()
        cur.close()
        conn.close()

    # Récupérer tous les blogs
    # Exécute un SELECT et récupère **toutes les lignes**
    # Retourne une liste d’objets Blog
    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, content, created_at, updated_at FROM blogs")
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        blogs = []
        for row in result:
            blogs.append(Blog(id=row[0], title=row[1], content=row[2], created_at=row[3], updated_at=row[4]))
        return blogs
       
    # Récupérer un blog par son ID
    # Exécute un SELECT avec une condition WHERE id=%s  
    # Si aucune ligne trouvée, retourne None
    # Sinon, transforme la ligne SQL → objet Blog et le retourne
    @staticmethod
    def get_by_id(blog_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, title, content, created_at, updated_at FROM blogs WHERE id=%s",(blog_id,))
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if result :
            return Blog(id=result[0], title=result[1], content=result[2], created_at=result[3], updated_at=result[4])
        else:   
            return None
        
    # Traduire le contenu du blog et générer un fichier audio
    def translate_and_speak(self, source_lang="auto", target_lang="en"):

        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(self.content)
        except Exception as e:
            return f"Erreur pendant la traduction : {str(e)}"

        # Générer une voix
        try:
            filename = f"blog_{self.id}_audio.mp3"
            tts = gTTS(translated, lang=target_lang)
            tts.save(filename)
        except Exception as e:
            return f"Erreur pendant la génération audio : {str(e)}"
        
        # Jouer selon l'OS
        try:
            osname = platform.system()
            if osname == "Windows":
                os.system(f"start {filename}")
            elif osname == "Darwin":  # macOS
                os.system(f"afplay {filename}")
            else:  # Linux
                os.system(f"mpg123 {filename}")
        except:
            pass 

    # Retour du texte traduit ---
        return translated

