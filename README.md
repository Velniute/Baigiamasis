Duomenys modeliui nuscrape‘inti iš www.autobilis.lt 2023-05-02.
Kodas:
from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Autobilis skelbimai'
sheet.append(["Marke", "Metai", "Kebulo_tipas", "Variklio_galia", "Kuro_tipas", "Pavaru_dezes_tipas", "Rida", "Kaina"])

for page_num in range(1, 162):
    source = requests.get(
        f'https://www.autobilis.lt/skelbimai/naudoti-automobiliai?order_by=created_at-desc&category_id=1&page={page_num}').text
    soup = BeautifulSoup(source, 'html.parser')
    blokai = soup.find('div', class_="search-rezult-container").find_all('div', class_="search-rezult-content")

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
            sheet.append([marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, rida, kaina])

        except Exception as e:
            pass

excel.save('Autobilis skelbimai_GALUTINIS.xlsx')

Kodo pristatymas:
1.	Importuojama biblioteka BeautifulSoup iš bs4 ir requests biblioteka.
2.	Sukuriamas tuščias excel failas naudojant openpyxl biblioteką, ir sukuriamas naujas lapas (sheet) pavadinimu "Autobilis skelbimai". Excel failas pasirinktas todėl, kad tikrinantis kaip veikia kodas susitaupo duomenų konvertavimo laikas iš csv. 
3.	Į sheet pirmąją eilutę pridedamos reikiamos stulpelių pavadinimai.
4.	Paleidžiamas ciklas, kuris iteruoja per puslapius nuo 1 iki 161. Tiek www.autobilis.lt svetainėje yra puslapių, kuriuose yra skelbimai.
5.	Užkraunama puslapio HTML turinio informacija naudojant requests biblioteką ir nustatomas numatytasis tekstų analizavimo (parsing) metodas "html.parser" naudojant BeautifulSoup biblioteką.
6.	Iš puslapio HTML turinio gaunami blokai (blokai yra HTML div elementai su klasės atributu "search-rezult-content").
7.	Užkraunamas vidinis ciklas, kuris iteruoja per kiekvieną bloką.
8.	Iš bloko gaunamos reikiamos informacijos apie automobilio markę, kainą, metus, kebulo tipą, variklio galią, kuro tipą, pavarų dėžės tipas, ir ridą, naudojant find() ir get_text() metodus.
9.	Gauta informacija patalpinama į sheet, naudojant sheet.append() metodą.
10.	Jei gaunama klaida, vykdomas except blokas.
11.	Išsaugojamas excel failas su visais surinktais duomenimis ir pabaigiama programa.

Gautas duomenų rinkinys iš 3108 eilučių. 

Sunkumai rašant kodą:
1. HTML kode informacija apie automobilio parametrus yra sudėti į tą patį bloką su ta pačia klase - „'div', class_="search-rezult-car-info", todėl jos „paėmimas“ galimas tik per teksto vietą,  o jei informacija nėra suvesta tvarkingai, nuskaitant reikšmės susimaišo: 
Dažniausiai nuskaitant informacija neteisingai „sukrisdavo“ į spalva ir rida stulpelius. Nusprendžiau atsisakyti spalvos kaip informacijos ir pasiėmiau kitą bloką, kur duomenys nusiskaitė kiek geriau:
Vis dėlto duomenis reikės tvarkyti, bet mažiau.  

2. Skelbimai išdėstyti per 162 svetainės polapius, todėl reikėjo papildomo kodo, kad būtų galima iteruoti per visus polapius renkant informaciją. 

3. Svetainėje yra išskirti TOP10 skelbimų, kurių div klasė yra kiek kitokia, kiek užtrukau kol supratau kodėl taip yra. 

4. Ieškojau kitos svetainės, kur automobilių parametrai būtų sudėti į skirtingus div, tai radau www.alio.lt, bet ten kilo problema, kad neina iteruoti per svetainės polapius, nes sistema tokia, kad scrolinant pasimato nauji skelbimai, bet URL nesikeičia, o scrape‘inant duomenis vis tiek pasiimdavau tik 25 skelbimus. 

5. Nedaug svetainių leidžia scrape‘inti autoskelbimus. 

