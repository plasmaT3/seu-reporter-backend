from flask import Flask
from app.routes import bp  # importa o blueprint principal
from app.routes_extras import extras_bp  # opcional, se tiver outro blueprint

app = Flask(__name__)

# Registra os blueprints
app.register_blueprint(bp)  # rotas principais
app.register_blueprint(extras_bp)  # rotas extras (se existir)

if __name__ == "__main__":
    app.run(debug=True)
