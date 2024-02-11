import bs4, requests, datetime, os

LINK = 'https://dgsaie.mise.gov.it/prezzi-settimanali-carburanti'
DATA_ATTUALE = datetime.datetime.now().strftime("%d.%m.%Y")
PREZZO_ATTUALE_FILE = f"prezzo_attuale_{DATA_ATTUALE}.txt"

def scrivi_su_file(file_path, contenuto):
    with open(file_path, 'w') as file:
        file.write(contenuto)

response = requests.get(LINK)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

settimanale_container = soup.find('div', class_='container-fluid py-4')
settimanale_a = settimanale_container.find_all('table', class_='table table-sm table-borderless')

main_title = None
output_content = ""

for table in settimanale_a:
    rows = table.find_all('tr')

    main_title = None
    output_content = "" 

    for row in rows:
        columns = row.find_all(['td', 'th'])

        prodotto_span = columns[0].find('span') if columns else None
        prodotto = prodotto_span.get_text(strip=True) if prodotto_span else ""

        if not prodotto:
            continue

        if prodotto_span and prodotto_span.has_attr('class') and 'text-primary' in prodotto_span['class']:
            main_title = prodotto
            output_content += f"\nTitolo: {main_title}\n"
            continue

        if main_title:
            if prodotto and prodotto != main_title:
                output_content += f"\nTitolo: {prodotto}\n"
            else:
                output_content += f"Prodotto: {prodotto}\n"

            prezzo = columns[1].get_text(strip=True)
            accisa = columns[2].get_text(strip=True)
            iva = columns[3].get_text(strip=True)
            netto = columns[4].get_text(strip=True)

            variazione_span = columns[5].find('span')
            variazione = variazione_span.get_text(strip=True) if variazione_span else ""

            output_content += f"Prezzo: {prezzo}\n"
            output_content += f"Accisa: {accisa}\n"
            output_content += f"IVA: {iva}\n"
            output_content += f"Netto: {netto}\n"
            output_content += f"Variazione: {variazione}\n\n"

    print("Ecco i Prezzi FUEL di questa settimana...")
    print(output_content)

scrivi_su_file(PREZZO_ATTUALE_FILE, output_content)
print(f"È disponibile il file '{PREZZO_ATTUALE_FILE}' con i prezzi di questa settimana.")