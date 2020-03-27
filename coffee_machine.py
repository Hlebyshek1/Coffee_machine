basewater = 400
basemilk = 540
basecoffbeans = 120
basecups = 9
basemoney = 550

def remanin():
    print("The coffee machine has: ")
    print(f"""{basewater} of water
{basemilk} of milk
{basecoffbeans} of coffee beans
{basecups} of disposable cups
${basemoney} of money""")
    wish1()

def fill():
    global basemoney,basecups,basecoffbeans,basemilk,basewater
    print("Write how many ml of water do you want to add:")
    water = int(input())
    basewater+=water
    print("Write how many ml of milk do you want to add:")
    milk = int(input())
    basemilk+=milk
    print("Write how many grams of coffee beans do you want to add:")
    grams = int(input())
    basecoffbeans+=grams
    print("Write how many disposable cups of coffee do you want to add:")
    cups = int(input())
    basecups+=cups
    wish1()

def take():
    global basemoney
    print(f"I gave you ${basemoney}")
    basemoney = 0
    wish1()

def buy():
    global basemoney,basecups,basecoffbeans,basemilk,basewater
    type_of_coffee = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "))
    if (type_of_coffee == "1"):
        if(0> basewater-250):
            print("Sorry, not enough water!")
        elif(0 > basecoffbeans-16):
            print("Sorry, not enough coffee!")
        elif (0>basecups-1):
            print("Sorry, not enough cups!")
        else:
            basewater -= 250
            basecoffbeans -= 16
            basecups -= 1
            basemoney += 4
            print("I have enough resources, making you a coffee!")
    elif(type_of_coffee == "2"):
        if(0> basewater-350):
            print("Sorry, not enough water!")
        elif(0>basemilk-75):
            print("Sorry, not enough milk!")
        elif(0 > basecoffbeans-20):
            print("Sorry, not enough coffee!")
        elif (0>basecups-1):
            print("Sorry, not enough cups!")
        else:
            basewater -= 350
            basemilk -= 75
            basecoffbeans -= 20
            basecups -= 1
            basemoney += 7
            print("I have enough resources, making you a coffee!")
    elif(type_of_coffee == "3"):
        if(0> basewater-200):
            print("Sorry, not enough water!")
        elif(0>basemilk-100):
            print("Sorry, not enough milk!")
        elif(0 > basecoffbeans-12):
            print("Sorry, not enough coffee!")
        elif (0>basecups-1):
            print("Sorry, not enough cups!")
        else:
            basewater -= 200
            basemilk -= 100
            basecoffbeans -= 12
            basecups -= 1
            basemoney += 6
            print("I have enough resources, making you a coffee!")
    else:
        print()
    wish1()


def wish1():
    wish= input("Write action (buy, fill, take, remaining, exit): ")
    if (wish == "fill"):
        fill()
    elif (wish == "take"):
        take()
    elif (wish == "buy"):
        buy()
    elif (wish == "remaining"):
        remanin()
    elif (wish == "exit"):
        return


wish1()
