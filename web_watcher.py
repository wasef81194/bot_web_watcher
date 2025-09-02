# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


URL = 'http://wasef.fr/'
CHECK_INTERVAL = 10

#Si la page n'est pas en js
'''#fonction qui effectue une requete sur le site en question
def get_site_content() :
    response = requests.get(URL)
    return response.text

#fonction qui recupere le contenu HTML sur le site en question
def extract_target_content(html) : 
    soup = BeautifulSoup(html, 'html.parser')
    #Exemple : extraire un élément par id
    target = soup.find(id="app")
    print('Target :  ', target.text)
    return target.text.strip() if target else None

def main():
    old_content = None
    while True : 
        html = get_site_content()
        current_content = extract_target_content(html)
        if old_content and current_content != old_content : 
            print('Attention : Le contenu à changer')
        else : 
            print('Pas de changement détecté')
        print(old_content, 'VS', current_content)
        old_content = current_content
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()'''

#Si la page est en JS
def get_site_content():
    # Configuration du navigateur en mode headless (sans interface graphique)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(URL)
    time.sleep(5)  # Attente pour que JS charge le contenu

    html = driver.page_source
    driver.quit()
    return html

def extract_target_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    target = soup.find(id="app")
    return target.text.strip() if target else None

def main():
    old_content = None
    while True:
        print(f"Verification a {time.strftime('%Y-%m-%d %H:%M:%S')}")
        html = get_site_content()
        current_content = extract_target_content(html)
        if current_content is None:
            print("Element cible non trouve.")
        elif old_content and current_content != old_content:
            print("Attention : le contenu a change !")
        else:
            print("Pas de changement detecte.")
        old_content = current_content
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()