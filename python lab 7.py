num1 = 1
while (num1 < 300):
    print num1
    num1 = num1 + 2
    
Mylist = [1,2,3,4,5,6,7,8,9,10]
index = 0
while (index < len(Mylist)):
    print Mylist[index]
    index = index + 1
    
import random
rand = random.randint(0,50)
userInput = -1
while(userInput != rand):
    userInput = int(raw_input())
    print userInput
    if rand == userInput:
        print "congratz"
    if rand < userInput:
        print "your too high"
    if rand > userInput:
        print "your too low"

   