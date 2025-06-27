from flask import Blueprint, jsonify
from app.services.trends_fetcher import fetch_trending_terms

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return jsonify({"message": "API do Seu Repórter funcionando!"})

@bp.route("/trending")
def trending():
    termos = fetch_trending_terms()
    return jsonify({"trending": termos})
