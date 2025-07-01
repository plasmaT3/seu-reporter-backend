import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# ✅ IMPORTAÇÃO AJUSTADA AQUI
from app.routes import bp as news_bp
from app.routes_extras import extras_bp

# Carrega o .env
load_dotenv()

# Configurações dinâmicas
frontend_url = os.getenv("FRONTEND_URL", "*")
is_debug = os.getenv("FLASK_ENV", "production") == "development"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": frontend_url}})

# Registro dos blueprints
app.register_blueprint(news_bp)
app.register_blueprint(extras_bp)

if __name__ == "__main__":
    app.run(debug=is_debug)
