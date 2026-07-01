import random
n=random.randint(1,100)

guesses=0

while True:
    guesses+=1
    a=int(input("Guess a number from 1 to 100:"))

    if (a==n) :
        break
        
    elif(a>n):
        print("please choose a lower number")

    else:
        print("please choose a higher number")

print(f"you have guessed the number correctly in {guesses} attemmpts.\n Thank you !")