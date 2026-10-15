import re
import json
import csv
from collections import Counter
from stop_words import stop_words 
import requests
from functools import reduce
import statistics


def get_data_url(url, api_key):
    header =  {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
    }
    params = {'api-key': api_key}
    try:
        response = requests.get(url, headers= header, params= params)

        if response.status_code == 200:
            print('data recuperer avec succe', response.status_code)
            data = response.json()
            return data
        else:
            print('erreur lors de la recuperation des données', response.status_code)
    except Exception as er:
        print('erreur', er)
        return None


pays = get_data_url('https://api.restcountries.com/countries/v5', 'rc_live_a3e9716983d94d59b71e30effdcb69cb')
print(pays)