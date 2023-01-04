#number guessing!
#basically the pogram will give numbers like 1-10 and you will have to guess which number it is!


import random
import webbrowser

#the program will choose a number.

print("Welcome to the number guessing game!")
ps = input('please choose the difficulty! \n 1.easy \n 2.medium \n 3.hard \n: ')


if ps == "easy":
    x = random.randint(0,10)
    #print(x)



    pw = int(input('please select a number betweeen 1-10: '))


    if pw == x:
        print('Number guessed!')
    
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

elif ps == "medium":
    x = random.randint(0,20)
    #print(x)



    pw = int(input('please select a number betweeen 1-20: '))


    if pw == x:
        print('Number guessed!')
    
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

elif ps == "hard":
    x = random.randint(0,50)
    #print(x)



    pw = int(input('please select a number betweeen 1-50: '))


    if pw == x:
        print('Number guessed!')
    
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')



else:
    print("something went wrong")



