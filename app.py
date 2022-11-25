from flask import Flask, render_template, request
from services.db_connection import DBConnection
from models.article_model import ArticleModel
from flask_cors import CORS
app = Flask(__name__)

CORS(app)


@app.route("/articles", methods=["POST", "GET"])
def insert_read_articles():
    db = DBConnection()
    if request.method == "POST":
        article = ArticleModel(
                request.json.get("sku"),
                request.json.get("name"),
                request.json.get("description"),
                request.json.get("price", 0),
                request.json.get("tags", []),
            )
        uid = db.insert(article.json())
        return {"uuid": str(uid)}
    else:
        return db.read()

@app.route("/articles/<_id>", methods=["GET"])
def read_article(_id):
    db = DBConnection()
    art = db.read(_id)
    art["_id"] = str(art["_id"])
    return art
    