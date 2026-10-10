
import random, string
from functools import reduce
from mymodule import countries
from data import pays
from datetime import datetime, date


def random_user_id():
    char = int(input('entrer un caractère: '))
    user_ID = int(input('entrer un user_ID: '))

    for _ in range(char):
        caracteres = string.ascii_letters + string.digits
        password = ''.join(random.choice(caracteres) for _ in range(user_ID))
        print(password)
    

def rgb_color_gen(nbr):
    l = []
    for _ in range(nbr):
        l.append(f'rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})')
    return l
    

def list_of_hexa_colors(n):
    lst = []

    for _ in range(n):
        nombre = f'#{random.randint(0, 0xFFFFFF):06x}'
        lst.append(nombre)
    return lst

def generate_colors(text, num):
    if text == "hexa":
        list_of_hexa_colors(num)
    elif text == "rgb":
        rgb_color_gen(num)
    else:
        print("erreur essaie encore")





def shuffle_list(ly):
    lm = []
    lst = ly  # On crée une copie pour ne pas détruire la liste d'origine

    for _ in range(len(lst)):
        nb = random.choice(lst)
        lm.append(nb)
        lst.remove(nb)

    return lm


def tab():
    T = []
    while len(T) < 7:
        nbr = random.randint(0, 9)
        if nbr not in T:
            T.append(nbr)
    return T

#l = [5, 7, 87, 42, 9, 0, 30]
#print('La liste d\'origine est: ',l)
#print('La liste mélangé est: ',shuffle_list(l))  # Renvoie la liste mélangée

# syntax
# Filtrons uniquement les nombres pairs
pays_nordique = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_melanger = ['Estonia', 'Asabeneh', 12, 4, 'Denmark']



def en_majuscule(chaine):
    return chaine.upper()

def lan_countries(payes):
    return 'E' in payes
def care(num):
    return num ** 2

grand_nombre = reduce(lambda x, y: x + y,
                      filter(lambda f : f % 2 == 0,
                            map(lambda x : x ** 2, numbers

                               )
                            )
                    )

print(grand_nombre)

concate = reduce(lambda acc, p: acc + ','+' ' + p , pays_nordique[:-1])
print(f'{concate} et {pays_nordique[-1]} sont des pays d\'Europe du Nord.' )

majuscule = list(map(en_majuscule, names))
print(majuscule)

land = list(filter(lan_countries, countries))
print(land)

squar = list(map(care, numbers))
print(squar)




pays_lanquage = map(lambda d: d['languages'], pays)

def nbr_language_parler(elements):
    dic = {}
    for element in elements:
        for u in element:
            if u in dic:
                dic[u] += 1
            else:
                dic[u] = 1
    return dic


import re
from collections import Counter


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(phrase):
    transf = re.sub(r"[%@#&$;!,.?]", '', phrase)
    return transf


print(clean_text(sentence))

def most_frequent_words(fuction):
    mots = re.findall(r'\b\w+\b', fuction.lower())
    compteur = Counter(mots)
    frequence = [(cpt, mot) for cpt, mot in compteur.most_common()]
    return frequence


print(most_frequent_words(clean_text(sentence)))
