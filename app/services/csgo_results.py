import requests
import os

PANDASCORE_API_URL = "https://api.pandascore.co/csgo/matches"
API_TOKEN = os.getenv("PANDASCORE_TOKEN")  # Coloque seu token no .env

def fetch_csgo_results():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"sort": "-begin_at", "per_page": 5}
    
    try:
        response = requests.get(PANDASCORE_API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        resultados = []
        for match in data:
            resultados.append({
                "name": match.get("name"),
                "status": match.get("status"),
                "begin_at": match.get("begin_at"),
                "opponents": [
                    opp["opponent"]["name"] for opp in match.get("opponents", [])
                ],
                "league": match.get("league", {}).get("name"),
                "serie": match.get("serie", {}).get("name"),
                "url": match.get("official_stream_url") or match.get("videogame", {}).get("slug"),
            })
        return resultados
    except Exception as e:
        print(f"Erro ao buscar resultados do CSGO: {e}")
        return []
