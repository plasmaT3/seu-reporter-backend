
from flask import jsonify
from app.routes import bp

@bp.route("/noticias/esports")
def noticias_esports():
    # TODO: integrar com HLTV e LoLEsports futuramente
    return jsonify({"categoria": "e-sports", "noticias": []})

@bp.route("/noticias/esportes")
def noticias_esportes():
    # TODO: integrar com fontes de esportes gerais (Ex: GloboEsporte, etc)
    return jsonify({"categoria": "esportes", "noticias": []})

@bp.route("/noticias/musica")
def noticias_musica():
    # TODO: coletar notícias de música
    return jsonify({"categoria": "música", "noticias": []})

@bp.route("/noticias/cinema")
def noticias_cinema():
    # TODO: coletar notícias de cinema
    return jsonify({"categoria": "cinema", "noticias": []})

@bp.route("/painel-esports")
def painel_esports():
    # TODO: coletar resultados da HLTV e LoLEsports
    return jsonify({"league_of_legends": [], "counter_strike_2": []})
