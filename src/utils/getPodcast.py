import requests
from bs4 import BeautifulSoup

# Lista de URLs de las páginas a analizar
urls = [
 "https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231221",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231214",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231207",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231130",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231123",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231116",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231109",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231102",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231026",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231019",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231012",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-231005",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230928",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230921",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230914",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230907",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230831",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230824",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230817",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230810",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230803",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230727",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230720",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230713",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230706",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230629",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230622",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230615",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230608",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230601",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230525",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230518",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230511",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230504",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230427",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230420",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230413",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230406",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230330",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230323",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230316",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230309",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230302",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230223",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230216",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230209",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230202",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230126",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230119",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230112",
"https://www.bbc.com/learningenglish/english/features/6-minute-english_2023/ep-230105"
]

# Función para obtener el href del enlace de descarga del PDF
def get_pdf_link(url):
    # Realizar una solicitud HTTP a la URL
    response = requests.get(url)
    
    # Parsear el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar el elemento <a> con la clase específica
    pdf_link_tag = soup.find("a", class_="download bbcle-download-extension-mp3")
    
    # Si el enlace se encuentra, devolver la URL
    if pdf_link_tag:
        return pdf_link_tag['href']
    else:
        return None

# Recorrer cada URL en la lista y obtener el enlace al PDF
for url in urls:
    pdf_link = get_pdf_link(url)
    if pdf_link:
        print(f"PDF Link: {pdf_link}")
    else:
        print("PDF Link not found.")
    print("-" * 60)
