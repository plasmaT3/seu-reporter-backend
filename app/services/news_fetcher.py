import feedparser

FEEDS = {
    "G1 Goiás": "https://g1.globo.com/rss/g1/goias/",
    "Mais Goiás": "https://www.maisgoias.com.br/feed/",
}

CATEGORIAS = {
    "política": ["governo", "senador", "presidente", "eleição", "prefeito", "vereador"],
    "economia": ["dinheiro", "economia", "preço", "inflação", "salário", "emprego", "negócio"],
    "segurança": ["assalto", "polícia", "crime", "roubo", "prisão", "delegacia"],
    "educação": ["escola", "educação", "professor", "universidade", "aluno", "enem"],
    "saúde": ["hospital", "doença", "vacina", "samu", "covid", "h1n1", "sus"],
    "tecnologia": ["tecnologia", "inteligência artificial", "ia", "chatgpt", "openai", "robô", "algoritmo", "machine learning", "deep learning"]
}


def classificar_categoria(titulo, resumo):
    texto = f"{titulo} {resumo}".lower()
    for categoria, palavras in CATEGORIAS.items():
        if any(palavra in texto for palavra in palavras):
            return categoria
    return "não classificada"


def fetch_goias_news(limit_per_feed=5, trending_terms=None):
    trending_terms = trending_terms or []
    trending_terms_lower = [t.lower() for t in trending_terms]

    noticias = []
    for nome_fonte, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_feed]:
            titulo = entry.title
            resumo = entry.get("summary", "")
            texto_completo = f"{titulo} {resumo}".lower()

            relevante = any(term in texto_completo for term in trending_terms_lower)
            categoria = classificar_categoria(titulo, resumo)

            noticias.append({
                "fonte": nome_fonte,
                "titulo": titulo,
                "link": entry.link,
                "publicado": entry.get("published"),
                "resumo": resumo,
                "relevante": relevante,
                "categoria": categoria
            })

    return noticias
