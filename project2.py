import random
randnumber = random.randint(1,100)
userguess = None
guesses = 0
while(userguess != randnumber):
    userguess=int(input("Enter your number : "))
    guesses += 1
    if(userguess==randnumber):
        print("Congratulations! You guessed it right.")
    else:
        if(userguess > randnumber):
            print("Sry! You guessed it wrong.Enter a smaller number.")
        else:
            print("Sry! You guessed it wrong.Enter a larger number.")
        

print(f"You guessed the number in {guesses} guesses.")
with open("highscore.txt","r") as f:
    highscore = int(f.read())
if(guesses<highscore):
    print("WOW!You have just broken the highscore!")
    with open("highscore.txt","w") as f :
        f.write(str(guesses))