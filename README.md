# Bitcoin Price and News Checker

#Day36 coding on python!

This Python script fetches the latest stock information for Bitcoin (BTC) in USD from Alpha Vantage API and checks if there's a significant change in the price. If the change is greater than 5%, it fetches the latest news related to Bitcoin from NewsAPI.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Setup

1. Get API keys from [Alpha Vantage](https://www.alphavantage.co/) and [NewsAPI](https://newsapi.org/).
2. Replace `stocks_api_key` and `news_api_key` variables with your API keys.

## Usage

1. Run the script.
2. It will print the headlines of the top three news articles related to Bitcoin if there's a significant change in the price.
