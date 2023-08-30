#  This is an example how to parse the sites which are forbidden to access

import requests, csv
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}


def get_school_names(url):
    with requests.Session() as req:
        req.headers.update(headers)
        r = req.get(url).text

        soup = BeautifulSoup(r, 'lxml')

        useful_infos = soup.find_all(class_="col-xs-12 col-md-4")
        file = open('dvfu_schools.csv', 'w', encoding='utf8', newline='')
        writer = csv.writer(file)
        writer.writerow(["id", "school name"])
        id = 0
        for _ in useful_infos:
            id += 1
            title = _.find(name="h4", class_="title").getText()
            writer.writerow([id, title])

        file.close()


url = 'https://www.dvfu.ru/schools/'
get_school_names(url)
