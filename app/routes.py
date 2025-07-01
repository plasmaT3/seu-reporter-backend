from flask import Blueprint, jsonify
from app.services.news_fetcher import (
    fetch_goias_news, fetch_general_news, fetch_tech_news
)
from app.services.esports import fetch_esports_news
from app.services.esportes import fetch_sports_news
from app.services.musica import fetch_music_news
from app.services.cinema import fetch_movie_news
from app.services.csgo_results import fetch_csgo_results

bp = Blueprint("routes", __name__)

@bp.route("/goias-news")
def goias_news():
    return jsonify({"noticias": fetch_goias_news()})

@bp.route("/general-news")
def general_news():
    return jsonify({"noticias": fetch_general_news()})

@bp.route("/tech-news")
def tech_news():
    return jsonify({"noticias": fetch_tech_news()})

@bp.route("/noticias/esports")
def esports_news():
    return jsonify({"noticias": fetch_esports_news()})

@bp.route("/noticias/esportes")
def sports_news():
    return jsonify({"noticias": fetch_sports_news()})

@bp.route("/noticias/musica")
def music_news():
    return jsonify({"noticias": fetch_music_news()})

@bp.route("/noticias/cinema")
def cinema_news():
    return jsonify({"noticias": fetch_movie_news()})

@bp.route("/noticias/csgo")
def csgo_results():
    return jsonify({"resultados": fetch_csgo_results()})
