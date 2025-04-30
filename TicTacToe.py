import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        
    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
        print("\n")
        
    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False
    
    def check_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        
        return False
    
    def check_tie(self):
        return " " not in self.board
    
    def ai_move(self):
        # Simple AI with some intelligence
        # First check for winning move
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_winner("O"):
                    return
                self.board[i] = " "
        
        # Then block player's winning move
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_winner("X"):
                    self.board[i] = "O"
                    return
                self.board[i] = " "
        
        # Try to take center
        if self.board[4] == " ":
            self.board[4] = "O"
            return
        
        # Try to take a corner
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for i in corners:
            if self.board[i] == " ":
                self.board[i] = "O"
                return
        
        # Take any available edge
        edges = [1, 3, 5, 7]
        random.shuffle(edges)
        for i in edges:
            if self.board[i] == " ":
                self.board[i] = "O"
                return
    
    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Enter positions 1-9 as shown below:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 \n")
        
        while True:
            self.board = [" " for _ in range(9)]
            self.current_player = "X"
            
            while True:
                self.print_board()
                
                if self.current_player == "X":
                    try:
                        position = int(input("Enter your move (1-9): ")) - 1
                        if position < 0 or position > 8:
                            print("Please enter a number between 1 and 9")
                            continue
                            
                        if not self.make_move(position):
                            print("That position is already taken!")
                            continue
                    except ValueError:
                        print("Please enter a valid number!")
                        continue
                else:
                    print("AI is thinking...")
                    self.ai_move()
                
                if self.check_winner(self.current_player):
                    self.print_board()
                    self.scores[self.current_player] += 1
                    print(f"Player {self.current_player} wins!")
                    break
                
                if self.check_tie():
                    self.print_board()
                    self.scores["Tie"] += 1
                    print("It's a tie!")
                    break
                
                self.current_player = "O" if self.current_player == "X" else "X"
            
            print("\nScores:")
            print(f"Player X: {self.scores['X']}")
            print(f"Player O: {self.scores['O']}")
            print(f"Ties: {self.scores['Tie']}")
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break

# Start the game
game = TicTacToe()
game.play()
