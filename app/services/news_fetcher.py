import feedparser

FEEDS = {
    "geral": [
        "https://g1.globo.com/rss/g1/",
        "https://rss.uol.com.br/feed/noticias.xml",
        "https://www.cnnbrasil.com.br/feed/",
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml"
    ],
    "goias": [
        "https://g1.globo.com/go/goias/rss/g1/",
        "https://www.jornalopopular.com.br/rss",
        "https://www.emaisgoias.com.br/feed/"
    ],
    "tecnologia": [
        "https://feeds.feedburner.com/GizmodoBrasil",
        "https://rss.tecmundo.com.br/feed",
        "https://www.cnet.com/rss/news/"
    ]
}

def fetch_news(feeds):
    news = []
    for feed_url in feeds:
        parsed = feedparser.parse(feed_url)
        for entry in parsed.entries[:5]:
            image_url = (
                entry.get("media_content", [{}])[0].get("url") or
                entry.get("media_thumbnail", [{}])[0].get("url") or
                entry.get("enclosures", [{}])[0].get("url") or
                None
            )
            news.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
                "image_url": image_url
            })
    return news

def fetch_goias_news():
    return fetch_news(FEEDS["goias"])

def fetch_general_news():
    return fetch_news(FEEDS["geral"])

def fetch_tech_news():
    return fetch_news(FEEDS["tecnologia"])
