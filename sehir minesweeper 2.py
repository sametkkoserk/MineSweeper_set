from swampy.TurtleWorld import*
import time
import random
def turtle_minesweeper():

    print('-------HELLO GAMERS-------\n')

    print('-------- First Turtle---------')
    name_1 = input('What is the name of Turtle one ?')
    while name_1 == ("") or name_1==" ":
        print("name cannot be empty:")
        name_1 = input("name of turtle one:")
    color_1 = input('Please select a color for your Turtle red-blue-green?')
    while color_1 !="red" and color_1 !="blue" and color_1!="green" :
        color_1=input("Please select a color for your Turtle red-blue-green:")




    print('\n-------- Second Turtle---------')
    name_2 = input('What is the name of Turtle two ?')
    while name_2 == ("") or name_1 == name_2 or name_2==" ":
        if name_1 == name_2:
            print("you have to write different name")
            name_2 = input("name of turtle two:")
        elif name_2 == ("") or name_2==" ":
            print("name cannot be empty")
            name_2 = input("name of turtle :")
    color_2 = input('Please select a color for your Turtle red-blue-green?')
    while (color_2 !="red" and color_2 !="blue" and color_2!= "green") or color_2==color_1:
        if color_2 !="red" and color_2 !="blue" and color_2!= "green" :
            color_2=input("Please select a color for your Turtle red-blue-yellow:")
        if color_1==color_2:
            color_2 = input("Please select a different color for your Turtle red-blue-green:")
    TurtleWorld().geometry("1000x300")
    turtle_1 = Turtle()
    turtle_1.x = -150
    turtle_1.y = 100
    turtle_1.color = color_1
    turtle_2 = Turtle()
    turtle_2.x = -150
    turtle_2.color = color_2
    def squares():
        turtle_1.set_delay(0.00000000001)
        turtle_2.set_delay(0.00000000001)
        turtle_1.pu()
        fd(turtle_1, 15)
        turtle_1.pd()
        rt(turtle_1,90)
        fd(turtle_1,2.5)
        for i in range(3):
            lt(turtle_1,90)
            fd(turtle_1,5)
        lt(turtle_1, 90)
        fd(turtle_1, 2.5)
        lt(turtle_1,90)
        turtle_1.pu()
        fd(turtle_1, 15)
        turtle_2.pu()
        fd(turtle_2, 15)
        turtle_2.pd()
        rt(turtle_2,90)
        fd(turtle_2,2.5)
        for i in range(3):
            lt(turtle_2,90)
            fd(turtle_2,5)
        lt(turtle_2, 90)
        fd(turtle_2, 2.5)
        lt(turtle_2,90)
        turtle_2.pu()
        fd(turtle_2, 15)
    for i in range(30):
        squares()
    def replace():
        bk(turtle_1, 900)
        bk(turtle_2, 900)
    replace()
    def background():
        turtle_1.set_delay(0.00000000001)
        turtle_2.set_delay(0.00000000001)
        turtle_1.pd()
        lt(turtle_1, 90)
        fd(turtle_1, 25)
        rt(turtle_1, 90)
        fd(turtle_1, 900)
        rt(turtle_1, 90)
        fd(turtle_1, 150)
        rt(turtle_1, 90)
        fd(turtle_1, 900)
        rt(turtle_1, 90)
        fd(turtle_1, 125)
        rt(turtle_1, 90)
        turtle_1.pu()

    background()
    bk(turtle_1,200)
    bk(turtle_2,200)
    bomb_1 = Turtle()
    bomb_2 = Turtle()
    bomb_3 = Turtle()
    bomb_4 = Turtle()
    bomb_5 = Turtle()
    bomb_6 = Turtle()
    bomb_7 = Turtle()
    bomb_8 = Turtle()
    bomb_9 = Turtle()
    bomb_10 = Turtle()
    liste=[bomb_1,bomb_2,bomb_3,bomb_4,bomb_5,bomb_6,bomb_7,bomb_8,bomb_9,bomb_10]
    i=0
    for i in range(5):
        liste[i].set_delay(0.000000001)
        liste[i].pu()
        liste[i].color="black"
        liste[i].x=-135
        liste[i].y=100
        i+=1
    ı=5
    for ı in range(5):
        liste[i].set_delay(0.01)
        liste[i].pu()
        liste[i].color="black"
        liste[i].x=-135
        i += 1
    a=5
    b=5
    c=5
    d=5
    e=5
    listecik=[a,b,c,d,e]
    for j in range(5):
        listecik[j]=int(random.uniform(4,29))

    sayac = 0
    for k in listecik:
        sayac +=1
        for l in range(sayac,5,1):
            while k == listecik[l]:
                listecik[l] = int(random.uniform(4,29))
    p=5
    for ö in range(5):
        for t in range(listecik[ö]):
            fd(liste[ö],30)
            fd(liste[p],30)
        p+=1



    fd(turtle_1,215)
    fd(turtle_2,215)

    turtle_1.pd()


    turtle_2.pd()

    turtle_1.set_pen_color(color_1)
    turtle_2.set_pen_color(color_2)


    total_1 = 0
    total_2 = 0
    print("Let’s start the game with a coin toss.")

    r = random.random()
    if (r <= 0.5):
        print("-------" + name_1 + " starts first-------")
    else:
        print("-------" + name_2 + " starts first-------")
    while total_1<29 and total_2<29:

        if (r <= 0.5):
            input("Please press ENTER to roll the dice " + name_1 + ":)")
            s = int(random.uniform(1, 7))
            if total_1 + s > 29:
                fd(turtle_1, 30*(29 - total_1))
                total_1 = 29

            else:
                fd(turtle_1, 30 * s)
                total_1 += s

            if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                print("BOOOM!!! "+name_1+" is eliminated")

                while total_2 < 29 :
                    input("Please press ENTER to roll the dice " + name_2 + ":)")
                    s = int(random.uniform(1, 7))
                    if total_2 + s > 29:
                        fd(turtle_2,30*(29 - total_2))
                        total_2 = 29
                    else:
                        fd(turtle_2, 30 * s)
                        total_2 += s
                    print("Dice result:" + str(s) + "\n")
                    print(name_2 + "'s total score is " + str(total_2) + "\n")
                    if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 ==listecik[3] or total_2 == listecik[4]:
                        print("BOOOM!!! "+name_2+" is eliminated")
                        break
                if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                    break
            else:
                print("Dice result:" + str(s) + "\n")
                print(name_1 + "'s total score is " + str(total_1))
                print(name_2 + "'s total score is " + str(total_2) + "\n")
            if total_1>=29 or total_2>=29:
                break
            while s == 6 and total_1 < 29:
                input("Please press ENTER to roll the dice " + name_1 + ":)")
                s = int(random.uniform(1, 7))
                if total_1 + s > 29:
                    fd(turtle_1, 30*(29 - total_1))
                    total_1 = 29

                else:
                    fd(turtle_1, 30 * s)
                    total_1 += s
                if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                    print("BOOOM!!! " + name_1 + " is eliminated")
                    while total_2 < 29 :
                        input("Please press ENTER to roll the dice " + name_2 + ":)")
                        s = int(random.uniform(1, 7))
                        if total_2 + s > 29:
                            fd(turtle_2, 30*(29 - total_2))
                            total_2=29

                        else:
                            fd(turtle_2, 30 * s)
                            total_2 += s
                        print("Dice result:" + str(s) + "\n")
                        print(name_2 + "'s total score is " + str(total_2) + "\n")
                        if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                            print("BOOOM!!! " + name_2 + " is eliminated")
                            break
                    if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                        break
                elif total_1<29 and total_2<29:
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1))
                    print(name_2 + "'s total score is " + str(total_2) + "\n")
            if total_1>=29 or total_2>=29:
                break
            input("Please press ENTER to roll the dice " + name_2 + ":)")
            s = int(random.uniform(1, 7))
            if total_2 + s > 29:
                fd(turtle_2, 30*(29 - total_2))
                total_2 = 29

            else:
                fd(turtle_2, 30 * s)
                total_2 += s
            if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                print("BOOOM!!! "+name_2+" is eliminated")
                while total_1 < 29 :
                    input("Please press ENTER to roll the dice " + name_2 + ":)")
                    s = int(random.uniform(1, 7))
                    if total_1 + s > 29:
                        fd(turtle_1, 30*(29 - total_1))
                        total_1 = 29

                    else:
                        fd(turtle_1, 30 * s)
                        total_1 += s
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1) + "\n")
                    if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                        print("BOOOM!!! " + name_1 + " is eliminated")
                        break
                if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                    break


            else:
                print("Dice result:" + str(s) + "\n")
                print(name_1 + "'s total score is " + str(total_1))
                print(name_2 + "'s total score is " + str(total_2) + "\n")

            if total_1>=29 or total_2>=29:
                break
            while s == 6 and total_2 < 29:

                input("Please press ENTER to roll the dice " + name_2 + ":)")
                s = int(random.uniform(1, 7))
                if total_2 + s > 29:
                    fd(turtle_2, 30*(29 - total_2))
                    total_2 = 29

                else:
                    fd(turtle_2, 30 * s)
                    total_2 += s
                if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                    print("BOOOM!!! " + name_2 + " is eliminated")
                    while total_1 < 29 :
                        input("Please press ENTER to roll the dice " + name_2 + ":)")
                        s = int(random.uniform(1, 7))
                        if total_1 + s > 29:
                            fd(turtle_1, 30*(29 - total_1))
                            total_1=29

                        else:
                            fd(turtle_1, 30 * s)
                            total_1 += s
                        print("Dice result:" + str(s) + "\n")
                        print(name_1 + "'s total score is " + str(total_1)+ "\n")
                        if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                            print("BOOOM!!! " + name_1 + " is eliminated")
                            break
                    if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                        break


                else:
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1))
                    print(name_2 + "'s total score is " + str(total_2) + "\n")
        else:


            input("Please press ENTER to roll the dice " + name_2 + ":)")
            s = int(random.uniform(1, 7))
            if total_2 + s > 29:
                fd(turtle_2, 30*(29 - total_2))
                total_2 = 29

            else:
                fd(turtle_2, 30 * s)
                total_2 += s

            if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                print("BOOOM!!! "+name_2+" is eliminated")
                while total_1 < 29 :
                    input("Please press ENTER to roll the dice " + name_2 + ":)")
                    s = int(random.uniform(1, 7))
                    if total_1 + s > 29:
                        fd(turtle_1,30*(29 - total_1))
                        total_1 = 29

                    else:
                        fd(turtle_1, 30 * s)
                        total_1 += s
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1) + "\n")
                    if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                        print("BOOOM!!! " + name_1 + " is eliminated")
                        break
                if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                    break

            else:
                print("Dice result:" + str(s) + "\n")
                print(name_1 + "'s total score is " + str(total_1))
                print(name_2 + "'s total score is " + str(total_2) + "\n")
            if total_1>=29 or total_2>=29:
                break
            while s == 6 and total_2 < 29:
                input("Please press ENTER to roll the dice " + name_2 + ":)")
                s = int(random.uniform(1, 7))
                if total_2 + s > 29:
                    fd(turtle_2, 30*(29 - total_2))
                    total_2 = 29

                else:
                    fd(turtle_2, 30 * s)
                    total_2 += s
                if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                    print("BOOOM!!! " + name_2 + " is eliminated")
                    while total_1 < 29 :
                        input("Please press ENTER to roll the dice " + name_2 + ":)")
                        s = int(random.uniform(1, 7))
                        if total_1 + s > 29:
                            fd(turtle_1, 30*(29 - total_1))
                            total_1=29

                        else:
                            fd(turtle_1, 30 * s)
                            total_1 += s
                        print("Dice result:" + str(s) + "\n")
                        print(name_1 + "'s total score is " + str(total_1)+ "\n")
                        if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                            print("BOOOM!!! " + name_1 +" is eliminated")
                            break
                    if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                        break


                else:
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1))
                    print(name_2 + "'s total score is " + str(total_2) + "\n")
            if total_1>=29 or total_2>=29:
                break

            input("Please press ENTER to roll the dice " + name_1 + ":)")
            s = int(random.uniform(1, 7))
            if total_1 + s > 29:
                fd(turtle_1, 30*(29 - total_1))
                total_1 = 29

            else:
                fd(turtle_1, 30 * s)
                total_1 += s
            if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                print("BOOOM!!! "+name_1+" is eliminated")
                while total_2 < 29 :
                    input("Please press ENTER to roll the dice " + name_2 + ":)")
                    s = int(random.uniform(1, 7))
                    if total_2 + s > 29:
                        fd(turtle_2, 30*(29 - total_2))
                        total_2 = 29

                    else:
                        fd(turtle_2, 30 * s)
                        total_2 += s
                    print("Dice result:" + str(s) + "\n")
                    print(name_2 + "'s total score is " + str(total_2) + "\n")
                    if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                        print("BOOOM!!! " + name_2 + " is eliminated")
                        break
                if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                    break
            else:
                print("Dice result:" + str(s) + "\n")
                print(name_1 + "'s total score is " + str(total_1))
                print(name_2 + "'s total score is " + str(total_2) + "\n")
            if total_1>=29 or total_2>=29:
                break
            while s == 6 and total_1 < 29:
                input("Please press ENTER to roll the dice " + name_1 + ":)")
                s = int(random.uniform(1, 7))
                if total_2 + s > 29:
                    fd(turtle_2, 30*(29 - total_2))
                    total_2 = 29

                else:
                    fd(turtle_2, 30 * s)
                    total_2 += s
                if total_1 == listecik[0] or total_1 == listecik[1] or total_1 == listecik[2] or total_1 == listecik[3] or total_1 == listecik[4]:
                    print("BOOOM!!!" + name_1 + " is eliminated")
                    while total_2 < 29 :
                        input("Please press ENTER to roll the dice " + name_2 + ":)")
                        s = int(random.uniform(1, 7))
                        if total_2 + s > 29:
                            fd(turtle_2, 30*(29 - total_2))
                            total_2=29

                        else:
                            fd(turtle_2, 30 * s)
                            total_2 += s
                        print("Dice result:" + str(s) + "\n")
                        print(name_2 + "'s total score is " + str(total_2) + "\n")
                        if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                            print("BOOOM!!! " + name_2 + " is eliminated")
                            break
                    if total_2 == listecik[0] or total_2 == listecik[1] or total_2 == listecik[2] or total_2 == listecik[3] or total_2 == listecik[4]:
                        break
                else:
                    print("Dice result:" + str(s) + "\n")
                    print(name_1 + "'s total score is " + str(total_1))
                    print(name_2 + "'s total score is " + str(total_2) + "\n")

    if total_1 >= 29:
        print("-------" + name_1 + " won-------")
    elif total_2 >= 29:
        print("-------" + name_2 + " won-------")
    else:
        print("no one could win the game")






turtle_minesweeper()
a=input("Would you like to play again yes/no:")
while a!="yes" and a!="no":
    a=input("please choose yes or no")
while a=="yes":
    turtle_minesweeper()
    a = input("Would you like to play again yes/no:")
    while a != "yes" and a != "no":
        a = input("please choose yes or no")
