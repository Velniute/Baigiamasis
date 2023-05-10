from bs4 import BeautifulSoup
import requests, openpyxl

# with open("data_autobilis/autobilis6.csv", 'w', encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(["Marke", "Metai", "Kebulo_tipas", "Variklio_galia", "Kuro_tipas", "Pavaru_dezes_tipas",
#                          "Saplva", "Rida", "Kaina"])

try:
    source = requests.get('https://caramba.lt/naudoti-automobiliai').text
    soup = BeautifulSoup(source, 'html.parser')
    blokai = soup.find('div', class_="container").find_all('div', class_="col-auto col-sm-6 col-md-4 col-lg-3 mb-20")
    print(len(blokai))

except Exception as e:
    print(e)

# for blokas in blokai:
#           try:
#              marke = blokas.find('div', class_="product-card__content").a.get_text
#              # kaina = blokas.find('div', class_="hidden-xs").span.text
#              # metai = blokas.find('div', class_="two-lines").get_text(strip=True).split('|')[0]
#              # kebulo_tipas = blokas.find('div', class_="product-card__model").get_text(strip=True)
#              # variklio_galia = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[2]
#              # kuro_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[3]
#              # pavaru_dezes_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[4]
#              # rida = blokas.find("li", class_="detail-list__item").li.text[0]
#
#             # print(marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, spalva, rida, kaina)
#             # csv_writer.writerow([marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, spalva,
#             #                      rida, kaina])
#
#           except Exception as e:
#             pass
#
# print(marke)



# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = 'Autobilis skelbimai'
# sheet.append(["Marke", "Metai", "Kebulo_tipas", "Variklio_galia", "Kuro_tipas", "Pavaru_dezes_tipas", "Rida", "Kaina"])


# for page_num in range(1, 162):
#     source = requests.get(
#         f'https://www.autobilis.lt/skelbimai/naudoti-automobiliai?order_by=created_at-desc&category_id=1&page={page_num}').text
#     soup = BeautifulSoup(source, 'html.parser')
#     blokai = soup.find('div', class_="search-rezult-container").find_all('div', class_="search-rezult-content")
#
#     for blokas in blokai:
#         try:
#             marke = blokas.find('div', class_="title").get_text(strip=True).split(',')[0]
#             kaina = blokas.find('div', class_="hidden-xs").span.text
#             metai = blokas.find('div', class_="two-lines").get_text(strip=True).split('|')[0]
#             kebulo_tipas = blokas.find('div', class_="two-lines").get_text(strip=True).split('|')[1]
#             variklio_galia = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[2]
#             kuro_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[3]
#             pavaru_dezes_tipas = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[4]
#             rida = blokas.find("div", class_="two-lines").get_text(strip=True).split('|')[5]
#
#             print(marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, rida, kaina)
#             sheet.append([marke, metai, kebulo_tipas, variklio_galia, kuro_tipas, pavaru_dezes_tipas, rida, kaina])
#
#         except Exception as e:
#             pass
#
#
# excel.save('Autobilis_skelbimai.xlsx')