
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def affiche_info(self):
            return f'le nom du joueur est {self.name} son symbole est {self.symbol} '

    def chose_name(self):
        name = input('entrez votre nom (uniquement des lettres): ')
        while not name.isalpha():
            print('nom invalide')
            name = input('entrez votre nom (uniquement des lettres): ')

        self.name = name
    

    def chose_symbol(self):
        symbol = input(f'{self.name} entrez un symbol (une seule lettre): ')
        while not symbol.isalpha() or len(symbol) != 1:
            print('Erreur veillez entrez une seule lettre: ')
            symbol = input(f'{self.name} entrez un symbol (une seule lettre): ')

        self.symbol = symbol
   

play1 = Player()
play1.chose_name()
play1.chose_symbol()
print(play1.affiche_info())


