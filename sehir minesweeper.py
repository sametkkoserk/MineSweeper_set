from swampy.TurtleWorld import*
import math
import random

def turtle_game():
    world = TurtleWorld()
    print('HELLOOOOOO')
    turtle_1 = Turtle()
    print('-------- First Turtle---------')
    name_1 = input('What is the name of Turtle one ?')
    while name_1 == (""):
        print("name cannot be empty:")
        name_1 = input("name of turtle one:")
    color_1 = input('Please select a color for your Turtle red-blue-yellow?')
    while color_1 !="red" and color_1 !="blue" and color_1!="yellow" :
        color_1=input("Please select a color for your Turtle red-blue-yellow:")
    turtle_1.color = color_1
    total_step_1 = 0
    def first_moving():
        turtle_1.pu()
        bk(turtle_1, 185)
    first_moving()

    turtle_2 = Turtle()
    print('-------- Second Turtle---------')
    name_2 = input('What is the name of Turtle two ?')
    while name_1 == name_2:
        print("you have to write different name:")

        def first_moving():
            turtle_1.pu()
            bk(turtle_1, 188)
        first_moving()
        name_2= input("name of turtle two:")
    while name_2 == (""):
        print("name cannot be empty:")
        name_2 = input("name of turtle :")
    color_2 = input('Please select a color for your Turtle red-blue-yellow?')
    while color_2 !="red" and color_2 !="blue" and color_2!= "yellow" :
        color_2=input("Please select a color for your Turtle red-blue-yellow:")
    while color_1==color_2:
        color_2 = input("Please select a different color for your Turtle red-blue-yellow:")
    turtle_2.color = color_2
    turtle_2.pu()
    bk(turtle_2, 188)
    rt(turtle_2, 90)
    fd(turtle_2, 70)
    lt(turtle_2, 90)
    total_step_2=0
    a = random.random()
    if (a <= 0.5):
        k = 1
        print("-------player1 first-------")
    else:
        k = 0
        print("-------player2 first-------")
    while total_step_1<350 and total_step_2<350:
        if k == 1:
            step_1=int(input("enter the step number"))
            c=random.uniform(1,175)
            if step_1 <= c:
                fd(turtle_1,step_1)
                total_step_1+=step_1
                print(name_1 + "'s total step is ", end="")
                print(int(total_step_1))
            else:
                print("you lost your right")
            if total_step_1 >= 350:
                break

            elif total_step_2 >= 350:
                break

            step_2 = int(input("enter the step number"))
            d = random.uniform(1, 175)
            if step_2 <= d:
                fd(turtle_2, step_2)
                total_step_2 += step_2
                print(name_2 + "'s total step is ", end="")
                print(int(total_step_2))
            else:
                print("you lost your right")
        if k==0:
            step_2 = int(input("enter the step number"))
            d = random.uniform(1, 175)
            if step_2<=d:
                fd(turtle_2,step_2)
                total_step_2+=step_2
                print(name_2 + "'s total step is ", end="")
                print(int(total_step_2))
            else:
                print("you lost your right")
            if total_step_1 >= 350:
                break

            elif total_step_2 >= 350:
                break

            step_1 = int(input("enter the step number"))
            c = random.uniform(1, 175)
            if step_1 <= c:
                fd(turtle_1, step_1)
                total_step_1 += step_1
                print(name_1+"'s total step is ",end="")
                print(int(total_step_1))
            else:
                print("you lost your right")
    if total_step_1>=350:
        print("-------"+name_1+" won-------")
    elif total_step_2>=350:
        print("-------"+name_2+" won-------")

    wait_for_user()
turtle_game()
