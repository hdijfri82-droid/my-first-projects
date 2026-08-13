import random

randomize = random.randint(1, 100)
guesses = 0
while True :
    try:
        number = int(input('insert your number ='))
        guesses += 1
        if number == randomize : 
            print ('you won')
            break

        elif number > randomize :
            print ('go down')

        else:
            print ('go up')

        if guesses > 7 :
            print(randomize)
            break

    except ValueError:
        print ('please insert number')
    
