import random

class FizzBuzz :
    def __init__ (self) :
        self.players_ = []

    def fizzBuzz (self, number) :
        if number%3 == 0 and number%5 == 0 :
            return 'FizzBuzz'

    def fizz (self, number) :
        if number%3 == 0 and number%5 != 0 :
            return 'Fizz'

    def buzz (self, number) :
        if number%5 == 0 and number%3 != 0 :
            return 'Buzz'
        
    def pass_ (self, number) :
        if number%5 != 0 and number%3 != 0 :
            return 'Pass'
        
    def checkPlayers (self, list_of_players, list_of_losers) :
        if len(list_of_losers) == len(list_of_players) -1 :
            return True
        
        
    def guess (self, guess) :
        if guess == '3' :
            guess = 'Fizz'
            return guess
        elif guess == '5' :
            guess = 'Buzz'
            return guess
        elif guess == '1' :
            guess = 'FizzBuzz'
            return guess
        elif guess == '0' :
            guess = 'Pass'
            return guess
        
    def players (self, members) :
        for i in range (1, members+1) :
            self.players_.append(f"player {i}")

    def play (self) :
        members = int(input("how many members will play this game"))
        self.players(members)
        list_of_losers = []
        while True :
            
            for i in range (len(self.players_)) :

                print(f"{self.players_[i]} will guess")
                self.number = random.randint(1,100)
                print(self.number)
                self.guess_ = input("""enter guess 
                                    3 for fizz
                                    5 for Buzz
                                    1 for FizzBuzz
                                    0 for Pass 
                                    """)
                if self.fizzBuzz(self.number) == self.guess (self.guess_) :
                    print(f"{self.players_[i]} won")
                elif self.fizz(self.number) == self.guess (self.guess_) :
                    print(f"{self.players_[i]} won")
                elif self.buzz(self.number) == self.guess (self.guess_) :
                    print(f"{self.players_[i]} won")
                elif self.pass_(self.number) == self.guess (self.guess_) :
                    print(f"{self.players_[i]} won")
                else :
                    print(f"{self.players_[i]} lost")
                    list_of_losers.append(f"{self.players_[i]}")
                
                    if self.checkPlayers(self.players_, list_of_losers) :
                        print(f"only one player is left")
                        break

            if not list_of_losers :
                pass
            else :
                for j in list_of_losers :
                    self.players_.remove(j)
                list_of_losers = []
                if len(self.players_) == 1 :
                    print(f"{self.players_[0]} is winner")
                    break

                
                    

            



game = FizzBuzz()
game.play()