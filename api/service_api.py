from random import randint
import requests
import json

def getAll():
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-key': "e43652d1dfmsh1006cb68ee19a97p1e5551jsnaaf407833714",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return(response.text)

def getCountry(region):
    url = f"https://restcountries.eu/rest/v2/region/{region}"
    response = requests.get(url)
    jsonCountry = json.loads(response.text)
    return jsonCountry[randint(0, len(jsonCountry)-1)]['name']

def getLanguage(country):
    url = f"https://restcountries.eu/rest/v2/name/{country}?fields=languages"
    response = requests.get(url)
    jsonLanguage = json.loads(response.text)
    return jsonLanguage[0]['languages'][0]['name']

