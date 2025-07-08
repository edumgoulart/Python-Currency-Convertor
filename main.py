import requests

#all_currencies = requests.get("https://api.frankfurter.dev/v1/currencies")
#print(all_currencies.json())

curr_in = input("Type the currency you have:").upper()

curr_out = input("Type the currency you want to convert:").upper()

amount = input(f"Type how much {curr_in} you want to convert:")

data = requests.get(f"https://api.frankfurter.dev/v1/latest?base={curr_in}&symbols={curr_out}")

print(data.json())