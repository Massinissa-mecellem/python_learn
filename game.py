
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

        self.symbol = symbol.upper()
   

class Manu:
    
    def display_manu_game(self):
        print('Welcom to X-O')
        print('1. Start game, 2. Quit game')
        choix = input('entrez votre choix: ')
        return choix
   


    def display_end_game(self):
        manu = """
        Game Over!
        Welcom to X-O
        1. Start game, 2. Quit game
        entrez votre choix: 
        """
        choix = input(manu)
        return choix
        
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
        
    def display_board(self, ):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("_"*5)
        
    
    def update_board(self, index, symbol):
        if self.isvalide_move(index):
            self.board[index - 1] = symbol
            return True
        return False
    
    def isvalide_move(self, index):
        return self.board[index - 1].isdigit()
            
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

        

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.manu = Manu()
        self.ccurent_player_index = 0

    def start_game(self):
        choise = self.manu.display_manu_game()
        if choise == '1':
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choise = self.manu.display_end_game()
                if choise == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break


    def play_turn(self):
        player = self.players[self.ccurent_player_index]
        self.board.display_board()
        print(f'{player.name}\'s turn ({player.symbol})')
        while True:
            try:
                cell_choise = int(input('chose your number in (1-9): '))
                if  1<= cell_choise <=9 and self.board.update_board(cell_choise, player.symbol):
                    break
                else:
                    print("invalid move")
            except ValueError:
                print('Please number beetwen 1-9')

        self.switch_player()

    def switch_player(self):
        self.ccurent_player_index = 1 - self.ccurent_player_index


    def check_win(self):
        liste_lop = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [0, 4, 8],
            [2, 4, 6],
            [2, 5, 8],
            [1, 4, 7]
            ]
        
        player = self.players[self.ccurent_player_index]
        for indx in liste_lop:
             if all(self.board.board[i] == player.symbol for i in indx):
                print(f'player {player.name} avec le symbole {player.symbol} a gagné')
                return True
        return False
       


    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
        

    def restart_game(self):
        self.board.reset_board()
        self.ccurent_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thank you for playing")


    def setup_player(self):
        for number, player in enumerate(self.players, start= 1):
            print(f'Player {number} entrez votre choix: ')
            player.chose_name()
            player.chose_symbol()
            print('-'*20)
                    

game = Game()

game.start_game()


