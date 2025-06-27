from pytrends.request import TrendReq

def fetch_trending_terms(limit=10):
    try:
        pytrends = TrendReq(hl='pt-BR', tz=0)
        trending_df = pytrends.trending_searches(pn='brazil')
        return trending_df[0].head(limit).tolist()
    except Exception as e:
        return [f"Erro ao acessar Google Trends: {str(e)}"]
