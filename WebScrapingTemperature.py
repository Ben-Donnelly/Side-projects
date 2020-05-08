import requests
from bs4 import BeautifulSoup
import operator

places = []
temps = []
overall = None


def temperature_now(pl, tmps):
    for i in range(len(tmps)):
        if tmps[i] == 'N/A':
            tmps[i] = int(-1000)  # If no temp available from site
    for i in range(len(tmps)):
        tmps = list(map(int, tmps))

    d = dict(zip(pl, tmps))

    d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

    for key, val in d.items():
        print("{0:60} {1}".format(key, val) + '℃')


def main():
    data = requests.get('https://www.timeanddate.com/weather/?low=4&sort=1')  # https://www.timeanddate.com/weather/?low=4&sort=1

    soup = BeautifulSoup(data.text, 'html.parser')
    for tr in soup.find_all('tr'):  # All tr elements
        for td in tr.find_all('td'):  # All td elements
            for a in td.find_all('a'):  # All a tags
                places.append(a.text)

    for tr in soup.find_all('tr'):
        for td in tr.find_all('td', {'class', 'website_class'}):  # rbi
            string = td.text.replace(u'\xa0°C', u'')  # Avoid parsing issue
            temps.append(string)
    temperature_now(places, temps)


if __name__ == '__main__':
    main()
