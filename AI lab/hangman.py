import random


hangman_stages = [
        '''
___________
  |        |
           |
           |
           |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
           | 
           |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
/          |
           |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
/ |        |
           |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
/ | \\      |
           |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
/ | \\      |
 /         |
           |
        ___|___
        ''',
        '''
___________
  |        |
  o        |
/ | \\      |
 / \\       |
           |
        ___|___
        '''
]

    
class Hangman :
    
    def __init__ (self) :
        self.words = {'fruite':['apple','banana','mango']}
        self.key1 = random.choice(list(self.words.keys()))
        self.items = self.words[self.key1]
        self.choice_item = random.choice(self.items)
        self.attempts = len(hangman_stages) - 1
        self.remaining_attempts = len(hangman_stages) - 1
        self.guesses = set()
        self.good_guess = set()
        
        

    def displayHangman (self) :
        self.stage_index = self.attempts - self.remaining_attempts
        print(hangman_stages[self.stage_index])



    def guess (self, guess) :
        self.flag = 0
        if guess in self.guesses :
            print('you\'ve already guessed it',guess)
            self.flag = 0
        else :
            self.guesses.add(guess)
            self.flag += 1

        if guess in self.choice_item :
            self.good_guess.add(guess)
            if all(letters in self.good_guess for letters in self.choice_item) :
                return True
        else :
            if self.flag != 0 :
                self.remaining_attempts -= 1
            return False
        
    def displayWord(self) :
        self.list1 = []
        for i in self.choice_item :
            if i in self.good_guess  :
                self.list1.append(i)
            else :
                self.list1.append('_')
        
        print(' '.join(self.list1))

    def play (self) :
        print("welcome to hangman!")
        print(f"guess the word {self.key1}")
        while self.remaining_attempts > 0 :
            self.displayHangman()
            self.displayWord()
            print(f'your remaining attempts {self.remaining_attempts}')
            self.user_input = input("enter your guess")
            if self.guess(self.user_input) :
                self.displayWord()
                print("congratulation on winning the game")
                break
        else :
            self.displayHangman()
            print("you have lost game")


game = Hangman ()
game.play()