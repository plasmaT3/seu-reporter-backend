from flask import Blueprint, jsonify

extras_bp = Blueprint("extras", __name__)

@extras_bp.route("/")
def index():
    return jsonify({"message": "API do Seu Redator está no ar"}), 200

@extras_bp.route("/noticias/esports")
def noticias_esports():
    return jsonify({"categoria": "e-sports", "noticias": []})

@extras_bp.route("/noticias/esportes")
def noticias_esportes():
    return jsonify({"categoria": "esportes", "noticias": []})

@extras_bp.route("/noticias/musica")
def noticias_musica():
    return jsonify({"categoria": "música", "noticias": []})

@extras_bp.route("/noticias/cinema")
def noticias_cinema():
    return jsonify({"categoria": "cinema", "noticias": []})

@extras_bp.route("/painel-esports")
def painel_esports():
    return jsonify({"league_of_legends": [], "counter_strike_2": []})
