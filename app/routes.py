from app.services.trends_fetcher import fetch_trending_terms
from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route("/")
@bp.route("/trending")
def trending():
    termos = fetch_trending_terms()
    return jsonify({"trending": termos})

def home():
    return jsonify({"message": "API do Seu Repórter funcionando!"})