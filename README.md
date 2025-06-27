# Seu Repórter Backend

API Flask para agregação de notícias e tendências do Google Trends.

## Como rodar localmente

```bash
python -m venv venv
.env\Scripts\Activate.ps1  # PowerShell
pip install -r requirements.txt
python -m app.main
```

## Deploy

Configurar no Render com start command:

```
gunicorn app.main:app --timeout 120
```
