# Importation des outils Flask
from flask import Flask, jsonify, request
#Importation de la classe Blog pour utiliser save(), get_all(), etc
from blog import Blog
# Création de l'application Flask
app = Flask(__name__)

# ROUTE : Creer un blog (POST) 
@app.route("/blogs",methods=["POST"])
def create_blog():
    data = request.json
    blog = Blog(title=data["title"],content=data["content"])
    blog.save()
    return jsonify(blog.to_dict())

# ROUTE : Obtenir tous les blogs (GET)
@app.route("/blogs", methods=["GET"])
def list_blogs():
    blogs = Blog.get_all()  # Récupère tous les blogs depuis la base
    # map retourne un map object, on le convertit en liste avec list() qui contient des dictionnaires de chaque blog
    blogs_json=list(map(lambda b: b.to_dict(), blogs))
    # Transforme les objets Blog en dictionnaires JSON
    return jsonify(blogs_json)

# ROUTE : Obtenir un blog par son ID (GET)
@app.route("/blogs/<int:id>", methods=["GET"])
def get_blog(id):
    blog = Blog.get_by_id(id) # Récupère le blog par son ID
    if not blog:
        return jsonify({"error": "not found"}), 404
    return jsonify(blog.to_dict())

# ROUTE : Mettre à jour un blog par son ID (PUT)
@app.route("/blogs/<int:id>",methods=["PUT"])
def update_blog(id):
    blog = Blog.get_by_id(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404

    data = request.json
    blog.title = data["title"]
    blog.content = data["content"]

    blog.update()
    return jsonify(blog.to_dict())

# ROUTE : Supprimer un blog par son ID (DELETE)
@app.route("/blogs/<int:id>",methods=["DELETE"])
def delete_blog(id):
    blog = Blog.get_by_id(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404

    blog.delete()
    return jsonify({"message": "Blog deleted"})

# ROUTE : Traduire un blog et générer un fichier audio (GET)
@app.route("/blogs/<int:id>/translate", methods=["GET"])
def translate_blog(id):
     
    # Récupère le blog par son ID
    blog = Blog.get_by_id(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404
    # Récupère les paramètres source et target de la requête
    
    source = request.args.get("source", "auto")
    target = request.args.get("target", "en")

    translated = blog.translate_and_speak(source, target)

    return jsonify({
        "id": blog.id,
        "original_title": blog.title,
        "original_content": blog.content,
        "translated_content": translated,
        "source_language": source,
        "target_language": target
    })

# /blogs/1/translate?source=fr&target=en
# /blogs/3/translate?source=en&target=ar

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
