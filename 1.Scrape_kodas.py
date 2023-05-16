import pandas as pd
from bs4 import BeautifulSoup
import requests
from sklearn.model_selection import train_test_split

#Sukuriau data lista, i kuri talpinsiu reiksmes
data = []

#Sukuriau 'for' cikla, kad atlikti HTTP užklausas autobilis.lt svetaines 161 puslapyje ir gauti HTML turinį iš kiekvieno puslapio
for page_num in range(1, 162):
    source = requests.get(
        f'https://www.autobilis.lt/skelbimai/naudoti-automobiliai?order_by=created_at-desc&category_id=1&page={page_num}').text
    soup = BeautifulSoup(source, 'html.parser')
    blokai = soup.find('div', class_="search-rezult-container").find_all('div', class_="search-rezult-content")

    #kodas leidžia pereiti per kiekvieną blokas objektą blokai sąraše ir išgauti informaciją apie automobilius (markę, metus, kainą ir tt.) 
    #iš HTML struktūros. Ši informacija spausdinama ekrane ir taip pat pridedama prie data sąrašo.
    for blokas in blokai:
        try:
            marke = blokas.find('div', class_="title").get_text(strip=True).split(',')[0]
            kaina = blokas.find('div', class_="hidden-xs").span.text
            metai = blokas.find('div', class_="two-lines").get_text(strip=True).split('|')[0]
            kebulo_tipas = blokas.find('div', class_="two-lines").get_text(strip=True).split('|')[1]
            variklio_galia = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[2]
            kuro_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[3]
            pavaru_dezes_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[4]
            rida = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[5]

            print(marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, rida, kaina)
            data.append({"Marke": marke, "Metai": metai, "Kebulo_tipas": kebulo_tipas, "Variklio_galia": variklio_galia,
                         "Kuro_tipas": kuro_tipas, "Pavaru_dezes_tipas": pavaru_dezes_tipas, "Rida": rida,
                         "Kaina": kaina})

        except Exception as e:
            pass

#kodas leidžia padalinti duomenis į mokymo ir testavimo rinkinius, pašalinti 'Kaina' stulpelį iš testavimo rinkinio ir išsaugoti mokymo ir 
#testavimo rinkinius kaip atskirus CSV failus.
train_data, test_data = train_test_split(pd.DataFrame.from_dict(data), test_size=0.3)

test_data.drop('Kaina', axis=1, inplace=True)

train_data.to_csv('train_duomenys.csv', index=False)
test_data.to_csv('test_duomenys.csv', index=False)
