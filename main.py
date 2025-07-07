import requests

all_currencies = requests.get("https://api.frankfurter.dev/v1/currencies")
print(all_currencies.json())