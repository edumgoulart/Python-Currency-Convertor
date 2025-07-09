import requests

#all_currencies = requests.get("https://api.frankfurter.dev/v1/currencies")
#print(all_currencies.json())

curr_in = input("Type the currency you have:").upper()

curr_out = input("Type the currency you want to convert:").upper()

amount = int(input(f"Type how much {curr_in} you want to convert:"))

#gets the value of the conversion rate
data = requests.get(f"https://api.frankfurter.dev/v1/latest?base={curr_in}&symbols={curr_out}")

conv_rate = data.json()["rates"][curr_out]

conv_amount = round(amount * conv_rate, 2)

print(f"Yours {amount} {curr_in} will be {conv_amount} {curr_out}.")


