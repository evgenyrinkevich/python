import requests
from xml.etree import ElementTree
import datetime


def currency_rates(valute):
    valute = valute.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ElementTree.fromstring(response.content)
    date_obj = datetime.datetime.strptime(tree.attrib['Date'], "%d.%m.%Y").date()
    # в задании требуется дата в формате date, не понятно зачем. Можно было просто tree.attrib['Date'],
    # так как выводим все равно в виде 30-Mar-2021
    for child in tree:
        if child[1].text == valute:
            result = child[4].text
            break
    else:
        result = None
    print(result, date_obj.strftime("%d-%b-%Y"))


if __name__ == '__main__':
    print(currency_rates('usd'))
