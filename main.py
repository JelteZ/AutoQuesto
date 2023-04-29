# input: wensen van klant.

# de AI gaat webscrapen.
def webScraping():
    print("Output: array van websites van de dealers")
    
# Kijkt op de website welke modellen auto's er allemaal verkocht worden.
def welkeAutos(websiteArray):
    print("Output: dictionary van auto's; merk: model")

# Kijkt welke merken en modellen het beste bij de wensen passen
def vergelijkAutos(wensArray, autoDict):
    print("Output: dictionary van gewenste auto's; merk: model")

# Vergelijkt verschillende Dealers en haalt sommige dealers weg als de kilometerStandWens niet past
def vergelijkDealers(aanraderDict, websiteArray, kilometerStandWens):
    print("Output: dictionary van merk + model: list van dealers met op list[0] de beste en op list[10] de slechtste")