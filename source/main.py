import portfolio
import order_manager
import position
import requests #pip install requests

initial_cash = input("Hello. How much cash can I trade with?")
#userPortfolio = portfolio(initial_cash)

#Gather data...
#JUST EXAMPLE GET, TODO: FIND BEST API
contents = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
print (contents.content)
