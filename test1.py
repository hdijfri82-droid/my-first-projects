import random

randomsaz = random.randint(1, 100)
guesses = 0
while True :
    try:
        karbar = int(input('adad ra vared konid ='))
        guesses += 1
        if karbar == randomsaz : 
            print ('barande shodid')
            break

        elif karbar > randomsaz :
            print ('paiin beravid')

        else:
            print ('bala beravid')

        if guesses > 7 :
            print(randomsaz)
            break

    except ValueError:
        print ('adad dorost vared konid')
    