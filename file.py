import re
import json
import csv
from collections import Counter
from stop_words import stop_words 
import requests
from functools import reduce
import statistics


def most_spoken_languages(filename, n):
    with open(filename, encoding= 'utf-8') as f:
        countries_data = json.load(f)
        all_language = Counter()
        for countrie in countries_data:
            all_language.update(countrie['languages'])
        return [(cpt, lang) for cpt, lang in all_language.most_common(n)]


def most_populated_countries(filename, n):
    with open(filename, encoding= 'utf-8') as f:
        countries_data = json.load(f)
        most_populated = sorted(
            countries_data, key=lambda c: c['population'], reverse=True
        )

        resultat = [{'country':c['name'], 'population':c['population']} for c in most_populated[:n]

        ]
        return resultat

def extract_email_address(file):
    with open(file) as f:
        address = f.read()
        emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', address, re.I)
        address_mail = list(set(emails))
        return address_mail
    


def find_most_common_words(filename, n):
    with open(filename) as f:
        lines= f.read()
        mots = re.findall(r'\b\w+\b', lines.lower())
        mot_frequent= Counter(mots)
        list_mots = [(cpt, word) for word, cpt in mot_frequent.most_common(n)]
        return list_mots






def clean_text(file):
    with open(file) as f:
        text = f.read()
        text_netoyer = re.sub(r'[^a-zA-Z\s]','', text.lower())
        list_text = []
        for word in text_netoyer.split():
            list_text.append(word)

        return list_text



def remove_support_words(file, fun):
    list_vide = []
    for word in fun:
        if word not in file:
            list_vide.append(word)
    return list_vide


michelle_words  = clean_text('./data/michelle_obama_speech.txt')
milina_words = clean_text('./data/melina_trump_speech.txt')
michelle_clean  = remove_support_words(stop_words, michelle_words)
milina_clean = remove_support_words(stop_words, milina_words)



def check_text_similarity(file_milina):
    score = 0
    pourcentage = 0
    for text_word in michelle_clean:
        if text_word in file_milina:
            score +=1
        else:
            print(f'les mots qui ne sont pas similaire est {text_word}')
    pourcentage = (score / len(michelle_clean)) * 100
    return f'le score de similarité est {pourcentage:.2f}%'


def get_word_romeo_juliet(romeo_and_juliet, n):
    with open(romeo_and_juliet, encoding='utf-8') as f:
        amor = f.read()
        clear_amour = re.sub(r'[^a-zA-Z\s]','', amor.lower())
        l = clear_amour.split()
        mot_repeter = Counter(l)
        reslt = [(cpt, word) for word, cpt in mot_repeter.most_common(n)]
        return reslt

    


def get_line_csv(filecsv):
    with open(filecsv, "r", encoding= 'utf-8') as f:
        sheet = csv.reader(f, delimiter=',')
        line_count = 0
        for row in sheet:
            if re.search(r"Java(?!Script)", row[1]):
                print(row[1])
                line_count +=1
        return line_count


def get_url(url):
    try:

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text
            return data

        else:
            print('erreur lors de la recupération des données', response.status_code)
            return None
        
    except Exception as e:
        print('Erreur du reseaux', e)
        return None

data_recuperer = get_url('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')



def get_cat_data(url):
    header = {
        "x-api-key": 'live_lvQLrgKMOhDFygybXGDbRSXnV1LG3BjaR1S6IXsLcPY5lGZJ7bug1h0m7s82KFv0',
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        ),
    }

    try:
    
        response = requests.get(url, headers= header)    
        if response.status_code == 200:
            data = response.json()
            return data
    
        else:
            print('erreur lors de la recupération des données', response.status_code)
            return None
            
    except Exception as e:
            print('Erreur du reseaux', e)
            return None

cats = get_cat_data('https://api.thecatapi.com/v1/breeds')



def get_life_span(data):
    esperence_vie = []
    for life in data:
        life_span = life['life_span']
        life_year = re.findall(r'\d+\.?\d*', life_span)
        for n in life_year:
            esperence_vie.append(int(n))
    return esperence_vie


def get_origine(data):
    origine_liste = []
    for pays in data:
        country = pays['origin']
        if country:

            origine_liste.append(country)
    return origine_liste
def get_name_cats(data):
    names = []
    for name in data:
        get_names = name['name']
        if get_names:
            names.append(get_names)
    return names

def get_freq(data):
    liste_pays = get_origine(data)
    mot_freq = Counter(liste_pays)
    return [(count, mots) for mots, count in mot_freq.most_common()]

def get_freq_names(data):
    liste_names = get_name_cats(data)
    count = Counter(liste_names)
    return [(cpt, name) for name, cpt in count.most_common()]

print(get_freq_names(cats))
print(get_freq(cats))