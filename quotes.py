import requests

quotes =[]

response = requests.get("https://type.fit/api/quotes")
response.raise_for_status()
quotes = response.json()