#####################################################################################################
# We are going to make a “Guess the Number” game. In this game, the computer will think of a        #
# random number from 1 to 20, and ask you to guess the number. You only get six guesses, but the    #
# computer will tell you if your guess is too high or too low. If you guess the number within six   #
# tries, you win.                                                                                   #
#####################################################################################################


import random
print("what is ur name ?")
myname = input()
number = random.randint(1, 20)
print('well, '+ myname + '  I think of a number between 1 to 20 , can u guess the number ?')
number_of_guess = 0
while number_of_guess < 6:
   get_number = input()
   get_number = int(get_number)

   number_of_guess = number_of_guess + 1

   if get_number > number:
       print("your guess is high")

   if get_number < number:
       print("your guess is low" )

   if get_number == number:
       break

if get_number == number:
    number_of_guess = str(number_of_guess)
    print('Good job, ' + myname + '! You guessed my number is ' + number_of_guess+ ' guesses!')

if get_number != number:
   number = str(number)
   print('you guesses are wrong ' + myname + ' the number was ' + number + ' ')
