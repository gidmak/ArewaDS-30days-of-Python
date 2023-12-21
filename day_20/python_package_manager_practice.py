
import requests
# Reading from url
url = 'https://gidmak.netlify.app' # text from a website

response = requests.get(url)
print(response)

# Reading from api
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)
print(url)