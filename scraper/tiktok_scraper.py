import os
import time
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv() #

LETTERS = list(string.ascii_lowercase)  

def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver #objet driver, qui contrôle Google Chrome via Selenium.

def scrape_suggestions(driver, letter):#return liste keywords from suggestion for one letter
    driver.get("https://www.tiktok.com")
    time.sleep(5)

    try:
        # Accepter cookies si présents *Tente de cliquer sur le bouton "Accepter" les cookies :
        try:
            accept = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accepter')]"))
            )
            accept.click()
            time.sleep(1)
        except:
            pass

        # Trouver la barre de recherche
        search_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Rechercher']"))
        )
        search_input.clear()
        search_input.send_keys(letter)
        time.sleep(2)

        # Attendre les suggestions
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//li[starts-with(@id, 'sug-list-item')]"))
        )
        #stock first 3 items in the liste
        items = driver.find_elements(By.XPATH, "//li[starts-with(@id, 'sug-list-item')]")
        return [item.text.strip() for item in items[:3] if item.text.strip()]

    except Exception as e:
        print(f"Erreur pour '{letter}' :", e)
        return []

def get_tiktok_keywords():#return all keywords for all the letters sous form de liste
    driver = load_driver() #Démarrage du navigateur
    keywords = []

    for letter in LETTERS:#appel a fct  scrape_suggestions for eatch letter and apprend it result to the iste keywords
        print(f"\n➜ Recherche pour la lettre : {letter}")
        result = scrape_suggestions(driver, letter)
        for suggestion in result:
            keywords.append(suggestion)
        print(f"  => Suggestions : {result}")

    driver.quit() #Ferme le navigateur
    return keywords
