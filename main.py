import requests

STOCK = "BTC"
COMPANY_NAME = "Bitcoin"

# Stocks infos
stocks_url = "https://www.alphavantage.co/query"
stocks_api_key = "JY2F55IRE1GQJUU0"

stocks_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": stocks_api_key
}
# News infos
news_url = "https://newsapi.org/v2/everything"
news_api_key = "154abd91a5f14f76b225a3bb2b45167a"

news_params = {
    "apiKey": news_api_key,
    "q": "Bitcoin",
    "from": "2024-02-07",
    "sortBy": "popularity", 
}

response = requests.get(stocks_url, params=stocks_params)
data = response.json()["Time Series (Digital Currency Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[1]
day_before_yesterday_data = data_list[2]

yesterday_price = float(yesterday_data["4b. close (USD)"])
day_before_yesterday_price = float(day_before_yesterday_data["4b. close (USD)"])

difference = abs(yesterday_price - day_before_yesterday_price)
diff_percent = (difference / float(yesterday_price)) * 100

if abs(diff_percent) > 5:
    news_response = requests.get(news_url, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formated_articles = [f"Headline: {article['title']}." for article in three_articles]

    print(formated_articles)