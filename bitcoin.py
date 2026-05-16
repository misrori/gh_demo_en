import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
response = requests.get(url, params=params)
data = response.json()
print(f"Bitcoin:  ${data['bitcoin']['usd']:,.0f}")
print(f"Ethereum: ${data['ethereum']['usd']:,.0f}")

