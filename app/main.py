import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Configurações
origins = os.getenv("CORS_ORIGINS", "*").split(",")
is_debug = os.getenv("DEBUG", "False").lower() in ["true", "1"]
port = int(os.getenv("PORT", 5000))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": origins}})

# Importa e registra blueprints CORRETAMENTE
from app.router import bp as news_bp
from app.router_extras import extras_bp

app.register_blueprint(news_bp)
app.register_blueprint(extras_bp)

if __name__ == "__main__":
    app.run(debug=is_debug, port=port)
