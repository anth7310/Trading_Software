# import subprocess
# subprocess.Popen(["python3", "some.file"])

# background process to download data from api
import database as db
import requests


# drop any existing tables
db.delete()
# create new table
db.create_table()

# ----- source 1 -----
# download data once
ticker = 'IBM'
interval = '5'
alphavantage_api_key = 'demo'
q = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}min&apikey={alphavantage_api_key}"

response = requests.get(q)
data = response.json()
for key in data.keys():
    if key.startswith('Time'):
        # get all dates from keys
        times = list(data[key])
        for time in times:
            # Example JSON: {'1. open': '135.3100', '2. high': '135.3100', '3. low': '135.3100', '4. close': '135.3100', '5. volume': '364'}
            # Example time: 2021-04-09 18:25:00
            open = data[key][time]['1. open']
            high = data[key][time]['2. high']
            low = data[key][time]['3. low']
            close = data[key][time]['4. close']
            # insert into database
            db.insert(ticker, time, float(open), float(high), float(low), float(close))

# ----- source 2 -----
# download data given interval
# https://finnhub.io/docs/api/quote
finnhub_api_key = ""
q = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={finnhub_api_key}"
r = requests.get(q)
data = r.json()

open = data['o']
high = data['h']
low = data['l']
close = data['c']
time = data['t'] # UTC ?
db.insert(ticker, time, float(open), float(high), float(low), float(close))

