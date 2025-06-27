import feedparser

FEEDS = {
    "G1 Goiás": "https://g1.globo.com/rss/g1/goias/",
    "Mais Goiás": "https://www.maisgoias.com.br/feed/",
}

def fetch_goias_news(limit_per_feed=5):
    noticias = []
    for nome_fonte, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_feed]:
            noticias.append({
                "fonte": nome_fonte,
                "titulo": entry.title,
                "link": entry.link,
                "publicado": entry.get("published"),
                "resumo": entry.get("summary"),
            })
    return noticias
