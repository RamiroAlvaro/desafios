# Your task: write a script to get a nice CSV file of natural gas prices.
#
# Please publish your results in a git repo or a gist. Please include both script and your resulting data – so the CSV
# files should be stored in the repo too!
#
# More detail:
#
# Prices should be Henry Hub gas prices. Use EIA data here: http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm 1
# Hint: you can get the data from any data source on the page …
# Main data wanted is daily prices.
# Bonus points for doing other granularities (e.g. month) - do them in separate CSV files with sensible naming
# Resulting CSV should have two columns: Date and Price. You may need to normalize the data to get this and/or work out
# dates. For months the Date should be the first date of the month.
# We want a script for this and we want this script to be in python (we’d allow node or bash or go script at a push but
# prefer python)
# Why a script? Ans: We’ll want to run this again and again as they release new data. You could copy and paste data into
# Excel/Google Docs by hand, and then export the CSV. But that would be tedious, time consuming and error prone to do
# month after month
# Please use simple python libraries wherever possible rather than use a framework
# Bonus items (optional - extra kudos if you do):
#
# Do a line graph visualization of the data in HTML + Javascript using e.g. vega or direct in D3
# Deploy your repo somewhere so this visualization is visitable online e.g. via github or gitlab pages


import csv
import datetime
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:

    bs = BeautifulSoup(html.read(), 'html.parser')

    weeks = bs.findAll('td', {'class': 'B6'})
    rows = bs.findAll('td', {'class': 'B3'})

    days = []
    regex = re.compile(r'(\d{4}) (\w{3})-(\s)?(\d{1,2})')
    for day in weeks:
        m = re.search(regex, day.get_text())
        date_str = f'{m.group(1)} {m.group(2)} {m.group(4)}'
        date_time_obj = datetime.datetime.strptime(date_str, '%Y %b %d')
        for i in range(5):
            days.append(f'{date_time_obj.date() + datetime.timedelta(days=i)}')

    # completing missing data with the previous or subsequent day
    for i, cell in enumerate(rows):
        if cell.get_text() == '' and i != len(rows) - 1 and rows[i + 1].get_text() != '':
            rows[i] = rows[i + 1]
        elif cell.get_text() == '' and i != 0 and rows[i - 1].get_text() != '':
            rows[i] = rows[i - 1]

    headers = ['Date', 'Price']
    csvRow = []

    for day, cell in zip(days, rows):
        csvRow.append((day, cell.get_text()))

    with open('date_price.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(csvRow)
