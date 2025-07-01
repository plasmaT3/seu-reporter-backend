from flask import Blueprint, jsonify
from app.services.news_fetcher import (
    fetch_goias_news, fetch_general_news, fetch_tech_news
)

bp = Blueprint("routes", __name__)

@bp.route("/noticias/goias")
def noticias_goias():
    return jsonify({"noticias": fetch_goias_news()})

@bp.route("/noticias/general")
def noticias_geral():
    return jsonify({"noticias": fetch_general_news()})

@bp.route("/noticias/tech")
def noticias_tecnologia():
    return jsonify({"noticias": fetch_tech_news()})
