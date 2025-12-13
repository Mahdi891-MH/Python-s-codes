import requests
from twilio.rest import Client

COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "Your news API key"
STOCK_KEY = "your stock price API key"
key = NEWS_KEY
q = "stock"

account_sid = "your Twilio sid"
auth_token = "your Twilio auth_token"

def stock_price():
    parameter = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "TSLA",
        "interval": "60min",
        "apikey": STOCK_KEY
    }
    response = requests.get(url=STOCK_ENDPOINT, params=parameter)
    stocks = response.json()["Time Series (60min)"]
    stocks_list = list(stocks)
    stock_prices = [float(stocks[stocks_list[0]]["4. close"]), float(stocks[stocks_list[16]]["4. close"])]
    difference = stock_prices[0] - stock_prices[1]
    percentage = difference*100/stock_prices[0]
    return percentage


def stock_news():
    parameter = {
        "q": COMPANY_NAME,
        "apiKey": key
    }
    response = requests.get(url=NEWS_ENDPOINT,params=parameter)
    response.raise_for_status()
    newses = response.json()["articles"]
    top_newses = newses[:3]
    if stock_price() < 0:
        prepared_news = f"TSLA: 🔻{-1*int(stock_price())}%\n"
    else:
        prepared_news = f"TSLA: 🔺{int(stock_price())}%\n"
    for news in top_newses:
        prepared_news+= f"Title: {news["title"]}\nBrief: {news["content"]}\n\n"

    return prepared_news


def send_message():
    if stock_price() * -1 >= 5:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=stock_news(),
            from_="+16204980485",
            to="your verified phone number"
        )
        print(message.status)

send_message()