class MovieBudget :
    
    def __init__ (self) :
        self.movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
        self.budget = []
        self.avg = 0

    def addMovies (self, no_ofMovies) :
        for i in range (no_ofMovies) :
            movie = input("enter movie name")
            budget = int(input("enter movie budget"))
            self.movies.append((movie,budget))

    def avgBudget (self) :
        for i in self.movies :
            self.budget.append(i[1])
        avg = sum(self.budget)/len(self.budget)
        self.avg = avg
        return avg
    
    def movieExceedFromAvg (self) :
        average = self.avgBudget(self.movies)
        for j in self.movies :
            if j[1] > average :
                self.movies.append(j[0])
                print(f"{j[0]} exceeds : {int((j[1]) - (average))}")
        print(f"{len(self.movies)} movies exceed from average budget")


calculator = MovieBudget ()
calculator.movies
# calculator.addMovies(3)
calculator.avgBudget()