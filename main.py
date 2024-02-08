import requests

STOCK = "BTC"
COMPANY_NAME = "Bitcoin"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stocks_url = "https://www.alphavantage.co/query"
stocks_api_key = "JY2F55IRE1GQJUU0"

stocks_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market": "USD",
    "apikey": stocks_api_key
}

response = requests.get(stocks_url, params=stocks_params)
data = response.json()["Time Series (Digital Currency Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_before_yesterday = data_list[1]

day_before_yesterday_price = float(day_before_yesterday["4b. close (USD)"])
last_day_price = float(yesterday_data["4b. close (USD)"])

difference = abs(last_day_price - day_before_yesterday_price)
diff_percent = (difference / float(last_day_price)) * 100

print(diff_percent)

# print(f"{day_before_yesterday_price:.2f}")
# print(f"{last_day_price:.2f}")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_url = "https://newsapi.org/v2/everything"
news_api_key = "154abd91a5f14f76b225a3bb2b45167a"

news_params = {
    "q": "Bitcoin",
    "from": "2024-02-07",
    "sortBy": "popularity", 
    "apiKey": news_api_key,
}


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

