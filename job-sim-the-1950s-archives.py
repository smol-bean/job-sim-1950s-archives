from time import sleep

def clear_output():
    for i in range(100):
        print("\n")
        

clear_output()
print(" you enter a office cubical that seems oddly familiar. a bot floats up to you.")
print("'hello welcome to a acurate simulation of OFFICE WORKER. take a slip and start the day.'")
print(" you look around and see and number of odd things. will you")
print("1: throw some thing at job bot.")
print("2: take a work slip")
print("3:take a work slip and throw it at job bot")
print("4: exit")
print("------------------------------------------------------------------------------------------------")
answer = input()
while True:
    if answer == "1":
        clear_output()
        print("you threw a stapler at job bot.")
        print("sparks flew from it.")
        print("1: exit")
        print("--------------------------------------------------------------------------------------------")
        answer = input()
        if answer == "1":
            clear_output()
            continue
    elif answer == "2":
        clear_output()
        print("you start your job")
        print("a floating cart goes up to your cubical")
        print("with a box of doughnuts and three coffee mugs.")
        print("'a human worker would usually start their day with a brown liquid stimulant.'")
        print("a board appears across from your cubical displaying a few images.")
        print("'follow the board for instructions'")
        print("1: pour yourself some coffee")
        print("2: throw a coffee mug at job bot")
        print("3: pour yourself some coffee and drink it and throw the coffee mug at job bot")
        print("4: exit")
        print("---------------------------------------------------------------------------------------------")
        answer = input()
    elif answer == "3":
        clear_output()
        print("you start your job by throwing the slip at job bot")
        print("'ow' sparks fly from job bot.")
        print("a floating cart goes up to your cubical")
        print("with a box of doughnuts and three coffee mugs.")
        print("'a human worker would usually start their day with a brown liquid stimulant.'")
        print("a board appears across from your cubical displaying a few images.")
        print("'follow the board for instructions'")
        print("1: pour yourself some coffee")
        print("2: throw a coffee mug at job bot")
        print("3: pour yourself some coffee and drink it and throw the coffee mug at job bot")
        print("4: exit")
        print("-------------------------------------------------------------------------------------------------")
        answer = input()
    if answer == "1":
        clear_output()
        sleep(3)
        print("you drink your coffee and as you drink the coffee the board images change")
        print("1: continue job")
        print("---------------------------------------------------------------------------------------------")
        answer = input()
        answer = "2"
    elif answer == "2":
        clear_output()
        print("you throw a mug at job bot.")
        print("sparks fly from the bot.")
        print("1: continue job")
        print("---------------------------------------------------------------------------------------------")
        answer = input()
        answer = "2"
    elif answer == "3":
        print("you drink you coffee and as you finish you here a ding from the board.")
        print("then you throw the coffee mug at job bot.")
        print("'good. humans would also often indulge in treats called DOUGHNUTS. take a DOUGHNUT and lets get moving.'")
        print("1: open the box and eat a doughnut")
        print("2: open the box and throw a doughnut at job bot")
        print("3: eat a doughnut then throw one it job bot")
        print("4: exit")
        print("---------------------------------------------------------------------------------------------")
    if answer == "4":
        break
clear_output()
print("come bock soon.")
sleep(3)
clear_output()
