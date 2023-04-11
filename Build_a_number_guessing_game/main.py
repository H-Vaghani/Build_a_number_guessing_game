class guessnumber:
    def __init__(self, number,min=0,max=100):
        self.number = number
        self.guess = 0
        self.min = min
        self.max = max
    def get_guess(self):
        guess = input(f"Guess the number ({self.min}) to ({self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("please enter a valid number: ")
            return self.get_guess()

    def valid_number(self,inputs):
        try:
            number = int(inputs)
        except:
            return False
        return self.min <= number <= self.max
    
    def play(self):
        while True:
            self.guess += 1

            guess = self.get_guess()

            if guess < self.number:
                print("go higher")
            elif guess > self.number:
                print("go less")
            else:
                break
        print(f"you guessed it in {self.guess} guesses.")

game = guessnumber(78,0,100)
game.play()