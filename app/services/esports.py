import feedparser

ESPORTS_FEEDS = [
    "https://www.hltv.org/rss/news",  # Notícias de CS2
    "https://www.dexerto.com/feed/"   # Notícias variadas (LoL, Valorant, etc)
]

def fetch_esports_news():
    noticias = []
    for url in ESPORTS_FEEDS:
        parsed = feedparser.parse(url)
        for entry in parsed.entries[:5]:
            media_content = entry.get("media_content")
            media_thumbnail = entry.get("media_thumbnail")
            enclosures = entry.get("enclosures")

            image_url = None
            if media_content and isinstance(media_content, list) and len(media_content) > 0:
                image_url = media_content[0].get("url")
            elif media_thumbnail and isinstance(media_thumbnail, list) and len(media_thumbnail) > 0:
                image_url = media_thumbnail[0].get("url")
            elif enclosures and isinstance(enclosures, list) and len(enclosures) > 0:
                image_url = enclosures[0].get("url")

            noticias.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
                "image_url": image_url
            })
    return noticias
