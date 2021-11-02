import os
import random
import numpy as np
from tabulate import tabulate

class Player:
    def __init__(self, number_player, ficha:str = "x", name_player: str = "CPU") -> None:
        self.ficha = ficha
        self.number_player = number_player
        self.name_player = name_player

class Board:
    def __init__(self,type_of_game: str = "CPU") -> None:
        self.board = np.chararray((4,4),unicode=True)
        self.player1 = Player(1, "x")        
        self.player2 = Player(2, "o")
        self.type_of_game = type_of_game

    def screen_clear(self):
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # for windows platfrom
            _ = os.system('cls')
        # print out some text

    #define some init variables
    def new_game(self):
        self.board[:] = '/'
        self.board[0,1] = 'a'
        self.board[0,2] = 'b'
        self.board[0,3] = 'c'
        self.board[1,0] = '1'
        self.board[2,0] = '2'
        self.board[3,0] = '3'
        self.player1 = Player(1, "x","CPU")        
        self.player2 = Player(2, "o","CPU")
        self.moves = list()
        self.draw = False
        self.winner_found = False
        self.turn = 0
        self.finish = False

    def init_message(self):
        print("Bienvenido a TIC TAC TOE.")

    def print_board(self):
        print("\n" + self.player1.ficha + ":" + self.player1.name_player, self.player2.ficha + ":" + self.player2.name_player)
        self.table = tabulate(self.board, tablefmt="grid")
        print(self.table)
        if(tablero.finish):
            if(self.winner_ficha == 3):
                print("Ha ganado",tablero.player1.ficha,"\n")
            elif(self.winner_ficha == -3):
                print("Ha ganado",tablero.player2.ficha,"\n")
            else:
                print("Empate")
            
    def select_player(self):
        print("Selecciona una ficha:\n1) x \n2) o")
        player_selected = input(">>> ")
        if(tablero.type_of_game == "player 2"):
            if (player_selected ==  tablero.player1.ficha):
                self.player1.name_player = "Usuario 1"
                self.player2.name_player = "Usuario 2"
            elif (player_selected ==  tablero.player2.ficha):
                self.player1.name_player = "Usuario 2"
                self.player2.name_player = "Usuario 1"
            else:
                print("\nError, debes escoger una ficha para jugar. Inténtalo otra vez.")
                print("1) x \n2) o")
                tablero.select_player()
        else:
            if (player_selected ==  tablero.player1.ficha):
                self.player1.name_player = "Usuario 1"
            elif (player_selected ==  tablero.player2.ficha):
                self.player2.name_player = "Usuario 1"
            else:
                print("\nError, debes escoger una ficha para jugar. Inténtalo otra vez.")
                print("1) x \n2) o")
                tablero.select_player()

    def select_type_of_game(self):
        print("Selecciona tipo de juego:\n1) CPU 2) player 2")
        self.type_of_game = input(">>> ")

    #generate a random move for the CPU player.
    def generate_cpu_move(self):
        column = ["a" ,"b" ,"c"]
        row = ["1", "2", "3"]
        move = random.choice(row) + random.choice(column)
        return move

    #check the cpu_move generated for avoid replaces.
    def control_cpu_move(self):
        move = tablero.generate_cpu_move()   
        while(move in self.moves):
            move = tablero.generate_cpu_move()
        return move 

    #check the user_move inputs for avoid replaces.
    def control_user_move(self):
        move = input(">>> ")  
        while(move in self.moves):
            print("Casilla ocupada. Intenta otra vez.")
            move = input(">>> ")
        return move 

    #core of the game
    def move_player(self,type_game):
        if (type_game == "CPU" and tablero.player1.name_player == "CPU" and self.turn % 2 == 0 and tablero.player1.number_player == 1):
            move = tablero.control_cpu_move()
            ficha = "x"
        elif(type_game == "CPU" and tablero.player2.name_player == "CPU" and self.turn % 2 == 1 and tablero.player2.number_player == 2):
            move = tablero.control_cpu_move()
            ficha = "o" 
        elif(self.turn % 2 == 0 and tablero.player1.number_player == 1):
            move = tablero.control_user_move()
            ficha = "x"
        else:
            move = tablero.control_user_move()
            ficha = "o" 
        
        self.moves.append(move)
        try:
            self.board[int(move[0]), int(ord(move[1]))-96] = ficha
            self.finish, self.winner_ficha = tablero.finish_winner()
            self.turn = self.turn + 1 
        except:
            print("Has introducido una posición incorrecta")
            tablero.move_player(tablero.type_of_game)
        
    
    #some codes for find the winner or draw
    #analyze rows
    def finish_winner(self):
        self.winner = 0
        for i in range(3):
            self.winner = 0
            for j in range(3):
                if (self.board[i+1,j+1] == "x"):
                    self.winner = self.winner + 1
                elif(self.board[i+1,j+1] == "o"):
                    self.winner = self.winner - 1
            if (self.winner == 3 or self.winner == -3):
                self.winner_found = True
                break

        #analyze columms        
        if(self.winner_found == False):
            for j in range(3):
                self.winner = 0
                for i in range(3):
                    if (self.board[i+1,j+1] == "x"):
                        self.winner = self.winner + 1
                    elif(self.board[i+1,j+1] == "o"):
                        self.winner = self.winner - 1
                if (self.winner == 3 or self.winner == -3):
                    self.winner_found = True
                    break
                    

        #analyze diagonal izquierda
        if(self.winner_found == False):
            self.winner = 0
            for i in range(3):
                if (self.board[i+1,i+1] == "x"):
                    self.winner = self.winner + 1
                elif(self.board[i+1,j+1] == "o"):
                    self.winner = self.winner - 1
                if (self.winner == 3 or self.winner == -3):
                    self.winner_found = True

        #analyze diagonal derecha
        if(self.winner_found == False):
            self.winner = 0
            for i in range(3):
                if (self.board[3-i,i+1] == "x"):
                    self.winner = self.winner + 1
                elif(self.board[3-i,i+1] == "o"):
                    self.winner = self.winner - 1
                if (self.winner == 3 or self.winner == -3):
                    self.winner_found = True  

        #analyze draw game
        if(self.winner_found == False):
            self.winner = 0
            for i in range(3):
                for j in range(3):
                    if (self.board[i+1,j+1] == "x"):
                        self.winner = self.winner + 1
                    elif(self.board[i+1,j+1] == "o"):
                        self.winner = self.winner + 1
                if (self.winner == 9):
                    self.winner_found = True
        return self.winner_found, self.winner

tablero = Board()
while(True):
    tablero.screen_clear()
    tablero.init_message()
    tablero.new_game()
    tablero.select_type_of_game()
    tablero.select_player()
    while(not tablero.finish):
        tablero.screen_clear()
        tablero.print_board()
        tablero.move_player(tablero.type_of_game)
    tablero.screen_clear()
    tablero.print_board()
    input("Press Enter to start a new game...")