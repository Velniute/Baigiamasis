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
