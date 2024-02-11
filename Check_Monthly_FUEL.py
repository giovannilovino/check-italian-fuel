import bs4
import requests

LINK = "https://dgsaie.mise.gov.it/prezzi-mensili-carburanti"

#check-HTTP
response = requests.get(LINK)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

# classe container del sito con tutti le informazioni
container_tabelle = soup.find('div', class_='container-fluid py-4')

# Trova tutti gli elementi <div> sotto 'container_tabelle'
dentro_container = container_tabelle.find_all('div', class_='col-md-6')

# Estrai il testo da ciascun elemento <div>
dati_DIV = []

for dati in dentro_container:
    nuovo_mese = dati.find('div', class_='card-header text-light font-weight-bold text-uppercase') #classe differente sul sito per il titolo del mese in evidenza
    altri_mesi = dati.find('div', class_='card-header font-weight-bold text-uppercase') #classe estrazione di tutti i titoli ad eccezione del primo / riga antecedente
    dati_carburante = dati.find_all('li', class_='list-group-item') #classe estrazione dati relativi ai carburanti
    
    # -> Itera i dati
    if nuovo_mese:
        titolo2_container = str(nuovo_mese.text)
        dati_DIV.append(titolo2_container)
    
    if altri_mesi:
        titolo_container = str(altri_mesi.text)
        dati_DIV.append(titolo_container)

    for i, benzina_element in enumerate(dati_carburante): #'view of output'
        testo_benzina = str(benzina_element.text)
        dati_DIV.append(testo_benzina)

        # riga bianca dopo l'ultimo elemento della lista 'view of output'
        if i == len(dati_carburante) - 1 and "O.C. denso BTZ" in testo_benzina:
            dati_DIV.append('\n')

# togli da lista / vai a capo
VOF_DIV = '\n'.join(dati_DIV)

#final print
print(VOF_DIV)





