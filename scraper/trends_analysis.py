from pytrends.request import TrendReq #outil Python non officiel pour interroger Google Trends.
import time

def get_trend_scores(keywords):
    print(" Analyse des mots-clés :", keywords)
    pytrends = TrendReq(
        hl='en-US',
        tz=60,
        requests_args={
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36'
            }
        }
    )#prepareconnexion a google trends en initialisant un objet
    time.sleep(5)  
    pytrends.build_payload(keywords, cat=0, timeframe='today 1-m')#envoir de requette
    return pytrends.interest_over_time()
