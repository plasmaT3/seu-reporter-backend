from flask import Blueprint, jsonify
from app.services.news_fetcher import (
    fetch_goias_news,
    fetch_general_news,
    fetch_tech_news
)
from app.services.esports import fetch_esports_news
from app.services.esportes import fetch_sports_news
from app.services.musica import fetch_music_news
from app.services.cinema import fetch_movie_news

bp = Blueprint("routes", __name__)

@bp.route("/goias-news")
def goias_news():
    noticias = fetch_goias_news()
    return jsonify({"noticias": noticias})

@bp.route("/general-news")
def general_news():
    noticias = fetch_general_news()
    return jsonify({"noticias": noticias})

@bp.route("/tech-news")
def tech_news():
    noticias = fetch_tech_news()
    return jsonify({"noticias": noticias})

@bp.route("/noticias/esports")
def esports_news():
    noticias = fetch_esports_news()
    return jsonify({"noticias": noticias})

@bp.route("/noticias/esportes")
def sports_news():
    noticias = fetch_sports_news()
    return jsonify({"noticias": noticias})

@bp.route("/noticias/musica")
def music_news():
    noticias = fetch_music_news()
    return jsonify({"noticias": noticias})

@bp.route("/noticias/cinema")
def cinema_news():
    noticias = fetch_movie_news()
    return jsonify({"noticias": noticias})
