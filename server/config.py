# api key for alphavantage
alphavantage_api_key = "GENWQYVH4N97XK5U"
finnhub_api_key = ""


ticker = ''
interval = ''
api_key = ''
request = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}min&apikey={alphavantage_api_key}"
