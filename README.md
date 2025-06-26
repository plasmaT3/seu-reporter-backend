# Seu Repórter - Backend

Backend em Flask para o projeto Seu Repórter.

## Como rodar localmente

```bash
pip install -r requirements.txt
python app/main.py
```

## Deploy no Render

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app.main:app`
- Variável de ambiente `PORT` já é utilizada automaticamente