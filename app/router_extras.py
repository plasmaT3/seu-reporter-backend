from flask import Blueprint, jsonify
from app.services.esportes import fetch_sports_news
from app.services.musica import fetch_music_news
from app.services.cinema import fetch_movie_news

extras_bp = Blueprint("extras", __name__)

@extras_bp.route("/")
def index():
    return jsonify({"message": "API do Seu Redator está no ar"}), 200

@extras_bp.route("/noticias/esports")
def noticias_esports():
    # Conteúdo temporário até integrar API real
    return jsonify({
        "noticias": [
            {
                "title": "CBLOL: LOUD vence e garante vaga antecipada",
                "summary": "Em confronto decisivo, a equipe da LOUD garantiu sua vaga nos playoffs do CBLOL...",
                "link": "https://lolesports.com",
                "image_url": "https://cdn.lolesports.com/news/cblol-placeholder.jpg"
            },
            {
                "title": "CS2: FURIA enfrenta NAVI em confronto tenso",
                "summary": "Brasileiros da FURIA jogam tudo mas caem diante dos ucranianos na ESL Pro League.",
                "link": "https://www.hltv.org",
                "image_url": ""
            }
        ]
    })


@extras_bp.route("/noticias/esportes")
def noticias_esportes():
    noticias = fetch_sports_news() or []
    return jsonify({"noticias": noticias})

@extras_bp.route("/noticias/musica")
def noticias_musica():
    noticias = fetch_music_news() or []
    return jsonify({"noticias": noticias})

@extras_bp.route("/noticias/cinema")
def noticias_cinema():
    noticias = fetch_movie_news() or []
    return jsonify({"noticias": noticias})

@extras_bp.route("/painel-esports")
def painel_esports():
    return jsonify({
        "league_of_legends": [],
        "counter_strike_2": []
    })
