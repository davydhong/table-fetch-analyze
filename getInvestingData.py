from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

################    SUPPORT FUNCTIONS #############


def getHTMLforResource(resource):
    """
    accepts a resource as a string input, and outputs an html table. The function makes a get request to investing.com. From the response HTML, the BeautifulSoup Library selects the table (data) element.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    reg_url = f"https://www.investing.com/commodities/{resource}-historical-data"
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    html = html.decode('utf-8')

    soup = BeautifulSoup(html)
    table = soup.find('table', {'class': 'genTbl closedTbl historicalTbl'})
    return table


def table2Arrays(table):
    """ accepts HTML table (parsed by BeautifulSoup) as an argument and parses data as an array of arrays.
    Only the date and price fields are parsed
    """
    headers = [field.text for field in table.find_all('th')]
    data = [field.text for field in table.find_all('td')]
    rows = [row[:2] for row in data2Rows(data, len(headers))]
    return (headers[:2], *rows)


def data2Rows(data, fieldCount):
    """the function breaks a list into chunks of fieldCount"""
    for i in range(0, len(data), fieldCount):
        yield data[i:i + fieldCount]


def writeCSV(resource, dataAsArray):
    with open(f'{resource}.csv', 'w', newline='') as csvfile:
        dataWriter = csv.writer(csvfile, delimiter='|')
        for row in dataAsArray:
            dataWriter.writerow(row)


################    Execution    #############

table = getHTMLforResource('gold')
rows = table2Arrays(table)
writeCSV('gold', rows)

table = getHTMLforResource('silver')
rows = table2Arrays(table)
writeCSV('silver', rows)

### stdout: date range of fetched data ###


def dateReformat(dateString):
    return datetime.strptime(dateString, '%b %d, %Y').strftime('%Y-%m-%d')


lastDate = dateReformat(rows[1][0])
firstDate = dateReformat(rows[-1][0])

print(f'date fetched from {firstDate} to {lastDate}')
