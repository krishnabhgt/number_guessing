import random
no = random.randint(1,9)
#print(no)
atempt =  0
while(no != "guess"):
    
    if(atempt == 3):
        print("you lost game")
        break
    guess = int(input("Guess any number 1 to 9 :"))
    if(guess > no):
        print("your guess is high")
    elif(guess < no):
        print("your guess is low")
    else:
        print("congrats you guessed it")
        break
    atempt += 1