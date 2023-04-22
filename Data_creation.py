import requests
from bs4 import BeautifulSoup



# Maak een lijst van de websites om te scrapen
websites = ["https://www.autoscout24.nl/", "https://www.marktplaats.nl/cp/91/auto-kopen/"]

# Maak een lege lijst om de links naar de advertenties op te slaan
links = []

# Maak een teller om het aantal gescrapte advertenties bij te houden
counter = 0

# Loop door elke website in de lijst
for website in websites:

    # Maak een unieke bestandsnaam voor elke advertentie
    filename = f"advertentie_{counter}.txt"
    # Maak een volledig pad naar de directory waar je het bestand wilt opslaan
    path = r"C:\Project 1 informatica\Trivauto\origineel"
    # Maak een bestand aan om de gegevens op te slaan
    f = open(path + "\\" + filename, "w")

    # Haal de HTML-code van de website op
    response = requests.get(website)

    # Parseer de HTML-code met BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Vind alle links naar de advertenties op de website
    # De links hebben verschillende attributen afhankelijk van de website
    if website == "https://www.autoscout24.nl/":
        # De links hebben het attribuut data-item-name="detail-page-link"
        link_elements = soup.find_all("a", {"data-item-name": "detail-page-link"})
    else:
        # De links hebben het attribuut class="mp-Listing-coverLink"
        link_elements = soup.find_all("a", {"class": "mp-Listing-coverLink"})

    # Voeg elke link toe aan de lijst van links
    for link_element in link_elements:
        link = link_element["href"]
        links.append(link)

# Loop door elke link in de lijst
for link in links:

    # Controleer of het maximum aantal gescrapte advertenties is bereikt
    if counter == 200000:
        break

    # Haal de HTML-code van de advertentie op
    response = requests.get(link)

    # Parseer de HTML-code met BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Vind de informatie over de auto op de advertentie
    # De informatie heeft verschillende tags en klassen afhankelijk van de website, Bing to the rescue!
    if link.startswith("https://www.autoscout24.nl/"):
        # De informatie heeft tags zoals h1, span, div en li met verschillende klassen
        merk = soup.find("h1", {"class": "cldt-detail-makemodel"}).text.strip()
        prijs = soup.find("span", {"class": "cldt-price"}).text.strip()
        kilometerstand = soup.find("div", {"class": "cldt-stage-basic-data"}).find("li", {"data-type": "mileage"}).text.strip()
        bouwjaar = soup.find("div", {"class": "cldt-stage-basic-data"}).find("li", {"data-type": "first-registration"}).text.strip()
        brandstof = soup.find("div", {"class": "cldt-stage-basic-data"}).find("li", {"data-type": "fuel"}).text.strip()
    else:
        # De informatie heeft tags zoals h1, span en dl met verschillende klassen
        merk = soup.find("h1", {"class": "mp-Listing-title"}).text.strip()
        prijs = soup.find("span", {"class": "mp-Listing-price"}).text.strip()
        kilometerstand = soup.find("dl", {"class":"mp-Listing-attributeList"}).find("dd", {"class": "mp-Listing-attributeList-item--mileage"}).text.strip()
        bouwjaar = soup.find("dl", {"class": "mp-Listing-attributeList"}).find("dd", {"class": "mp-Listing-attributeList-item--year"}).text.strip()
        brandstof = soup.find("dl", {"class": "mp-Listing-attributeList"}).find("dd", {"class": "mp-Listing-attributeList-item--fuel"}).text.strip()

    # Schrijf de informatie over de auto naar het bestand in een gestructureerd formaat
    f.write(f"Merk: {merk}\n")
    f.write(f"Prijs: {prijs}\n")
    f.write(f"Kilometerstand: {kilometerstand}\n")
    f.write(f"Bouwjaar: {bouwjaar}\n")
    f.write(f"Brandstof: {brandstof}\n")
    f.write("\n")

    # Verhoog de teller met 1
    counter += 1

# Sluit het bestand
f.close()

# Print een bericht dat het programma klaar is
print(f"Klaar! Er zijn {counter} autoadvertenties gescraped en opgeslagen in autoadvertenties.txt.")