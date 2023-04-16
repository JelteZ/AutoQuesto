import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Geef het pad op van het gedownloade webdriver-bestand
webdriver_path = "C:\\Users\\jelte\\Downloads\\edgedriver_win64\\msedgedriver.exe"
input_dir = "C:\\Project 1 informatica\\Trivauto\\origineel"
teller = 1

# Lijst van webpagina-URL's om te scrapen
url_list = ['https://www.autoscout24.nl/aanbod/volkswagen-passat-variant-1-4-tsi-gte-highline-btw-elektro-benzine-grijs-f802f46f-adfb-4421-b708-fe753de68ccb?sort=standard&desc=0&lastSeenGuidPresent=true&cldtidx=10&position=10&search_id=1t1wjgkrl65&source_otp=t30&source=listpage_search-results&order_bucket=2',
            'https://www.autoscout24.nl/aanbod/fiat-500-1-0-hybrid-2021-elektro-benzine-wit-1e6589e3-bbdd-40ff-aa62-f99351f75ad8?sort=standard&desc=0&lastSeenGuidPresent=true&cldtidx=15&position=15&search_id=1t1wjgkrl65&source_otp=t30&source=listpage_search-results&order_bucket=2',
            'https://www.autoscout24.nl/aanbod/volkswagen-jetta-1-4-tsi-hybrid-comfortline-elektro-benzine-zwart-d5d284bf-462c-4cce-b1f0-76daced0aa15?sort=standard&desc=0&lastSeenGuidPresent=true&cldtidx=17&position=17&search_id=1t1wjgkrl65&source_otp=t30&source=listpage_search-results&order_bucket=2']

# Loop door elke URL in de lijst
for url in url_list:
    # Start een nieuwe browserinstantie
    browser = webdriver.Chrome(executable_path=webdriver_path)

    # Open de gewenste website
    browser.get(url)

    # Selecteer de elementen waaruit je gegevens wilt ophalen
    elementen = browser.find_elements(By.TAG_NAME, 'p')

    # Maak een map aan om het .txt-bestand op te slaan
    mapnaam = input_dir

    # Creëer een bestandsnaam voor het .txt-bestand, bijvoorbeeld: 00023.txt
    bestandsnaam = '{0:05d}.txt'.format(teller)

    #verhoog de teller zodat de naam oploopt van 1 tot 99999
    teller += 1



    # Creëer een absoluut pad naar het .txt-bestand
    bestandspath = os.path.abspath(os.path.join(mapnaam, bestandsnaam))

    # Loop door de geselecteerde elementen en schrijf de gewenste gegevens naar het .txt-bestand
    with open(bestandspath, 'w', encoding='utf-8') as f:
        for element in elementen:
            f.write(element.text + '\n')

    # Sluit de browser af
    browser.quit()