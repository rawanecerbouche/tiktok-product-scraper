# main.py
from scraper.tiktok_scraper import get_tiktok_keywords
from scraper.trends_analysis import get_trend_scores
import pandas as pd
import os

def split_into_chunks(lst, chunk_size):
    """Divise une liste en sous-listes de taille maximale chunk_size"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

if __name__ == "__main__":
    #cree ficgier data
    os.makedirs("data", exist_ok=True)

    # Récupère les mots-clés depuis TikTok
    keywords = get_tiktok_keywords()
    print("🔍 Mots-clés récupérés depuis la barre de recherche TikTok :", keywords)

    if not keywords:
        print("❌ Aucun mot-clé trouvé. Vérifie la connexion ou le site TikTok.")
    else:
        all_trends = pd.DataFrame()#tableau vide df

        # Decoupe keywords en paquets de 5 mots
        for group in split_into_chunks(keywords, 5):
            print(f"📈 Analyse de ce groupe : {group}")
            try:
                trends = get_trend_scores(group)
                all_trends = pd.concat([all_trends, trends], axis=1)
            except Exception as e:
                print(f"Erreur pour {group} :", e)

        # Supprime les colonnes en double si des dates ont été fusionnées
        all_trends = all_trends.loc[:, ~all_trends.columns.duplicated()]

        # Sauvegarde le fichier
        all_trends.to_csv("data/keywords.csv")
        print("✅ Fichier exporté avec succès dans data/keywords.csv")
