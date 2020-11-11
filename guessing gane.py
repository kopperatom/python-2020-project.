## Kian Johnson
#9/20
# guess my number 1.0

import random


#intro
print ("\twelcome to  'guess my number' ! ")

question = input ("what difficulty would you like easy, medium, hard" )

if  (" Ea " in question) or ("ea" in question) :  #e or E puestion
    diff = 1
    maxrange = 10
    trys = 3
elif (" M " in question) or ("m" in question) :
     diff = 1
     maxrange = 50
     trys = 5
else:
     diff = 1
     maxrange =100
     trys = 10

     thenumber = random.randint (1,10)
print (thenumber)#shoes the number for debugging remove when done

print ("\nI'm thinking of a number between 1 and "+str (maxrange) +".")
print ("try to guess it in "+str (trys) +"  attempts .\n")

#win condition
winner = False

# guess 1
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
# guess 2
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
# guess 3
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")

#gues 4
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
#guess 5
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
# guess 6
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
#guess 7
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
#guess 8
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
# guess 9
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")
#guess 10
guess = int(input("pick a number between 1 and "+str (maxrange) ) )

if winner == False :
    if guess == thenumber:
        winner = True

elif guess <thenumber :
            print ("guess higher")

else :
                print ("guess lower")


# end condition
if winner == true:
    print ( "you are the winner")

