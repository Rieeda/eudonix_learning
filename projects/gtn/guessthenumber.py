#!/bin/python3.4
from random import randint

i = 0
a = 0
while a <= 0:
    a = input ("How many games?: ")
    try:
        a = int(a)
    except ValueError:
        print ("not a number!")
        a = 0

        
print("Okay we play %s 'Guess a number between 1 and 25' games!" %a)
        
while i < a:
    x =  randint(1,25)
    c = 0
    b = 0
    i += 1
    print("starting round %s" %i)
    while x != b:
        c += 1
        b = input ("Guess the number between 1 and 25: ")
        try:
            b = int(b)
        except ValueError:
            print("not a number!")
            b= 0
        if b == x:
            print("You got it! Number to guess was: %s " %b)
            print("You needed %s tries" %c)
            break
        elif b == 0:
            pass
        elif b < x:
            print("to low")
            c +=1
        else: 
            print("to high")
            c +=1
              
