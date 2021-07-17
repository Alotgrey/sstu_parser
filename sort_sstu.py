import requests
from bs4 import BeautifulSoup

f_i_o = input('Введите ФИО: ')
url = input('Дайте ссылку на то направление в СГТУ, на которое вы подали документы: ')
student_ege = []
urls = {}

soup = requests.get(url)
soup = BeautifulSoup(soup.text, 'lxml')

table = soup.find_all('table')
try:
        table = table[2]
except:
    try:
        table = table[1]
    except:
        table = table[0]
tbody = table.find('tbody')
trs = tbody.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    fio_now = tds[1]
    if f_i_o in fio_now.text:
        student_ege = [int(tds[2].text), int(tds[6].text)]
        hrefs = tds[1].find_all('a')
        for a in hrefs:
            urls[a.text] = 'https://abitur.sstu.ru/' + a.get('href')
        break

def print_Place(link, result):
    place_now = 1
    soup = requests.get(link)
    soup = BeautifulSoup(soup.text, 'lxml')

    table = soup.find_all('table')
    try:
        table = table[2]
    except:
        try:
            table = table[1]
        except:
            table = table[0]
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        place_now += ((int(tds[2].text) > result[0]) or ((int(tds[2].text) == result[0]) and (int(tds[6].text) > result[1]))) and (not "Отозвано" in tds[6].text)
    return place_now
for i in urls.keys():
    place = print_Place(urls.get(i), student_ege)
    print('На ' + i + ' Вы на ' + str(place) + ' месте.')
exit_b = input('Нажмите enter, чтобы выйти из программы')


    
    