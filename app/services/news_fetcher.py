import feedparser

FEEDS = {
    "G1 Goiás": "https://g1.globo.com/rss/g1/goias/",
    "Mais Goiás": "https://www.maisgoias.com.br/feed/",
}

def fetch_goias_news(limit_per_feed=5, trending_terms=None):
    trending_terms = trending_terms or []
    trending_terms_lower = [t.lower() for t in trending_terms]

    noticias = []
    for nome_fonte, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_feed]:
            titulo = entry.title.lower()
            resumo = entry.get("summary", "").lower()
            # Verifica se algum termo trending está no título ou resumo
            relevante = any(term in titulo or term in resumo for term in trending_terms_lower)
            noticias.append({
                "fonte": nome_fonte,
                "titulo": entry.title,
                "link": entry.link,
                "publicado": entry.get("published"),
                "resumo": entry.get("summary"),
                "relevante": relevante
            })
    return noticias
