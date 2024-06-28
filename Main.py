import math

print("Welcome to the GC Fruit Market!")
User_name = input("What is your name? " )

Fruit = ["Apple $2", "Grapes $1", "Orange $3"]
Greeting = (f"Welcome {User_name}. Which fruit would you like to buy?")
Summary = (f"Receipt for {User_name}")
print(Greeting)
print(f"1) {Fruit[0]}")
print(f"2) {Fruit[1]}")
print(f"3) {Fruit[2]}")
selection = input("> ")

apple_count = 0
grape_count = 0
orange_count = 0
cost = 0
while True:
    if selection == "1":
        print("You bought 1 apple at $2")
        apple_count += 1
        cost += 2

    elif selection == "2":
        print("You bought 1 grape at $1")
        grape_count += 1
        cost += 1

    elif selection == "3":
        print("You bought 1 orange at $3")
        orange_count += 1
        cost += 3

    else:
        print(f"Sorry. {selection} is an invalid option.")

    while True:
        response = input("Would you like to buy another piece of fruit? y/n ")
        if response == "y":

            print (Greeting)
            print(f"1) {Fruit[0]}")
            print(f"2) {Fruit[1]}")
            print(f"3) {Fruit[2]}")
            selection = input("> ")

            if selection == "1":
                print("You bought 1 apple at $2")
                apple_count += 1
                cost += 2

            elif selection == "2":
                print("You bought 1 grape at $1")
                grape_count += 1
                cost += 1

            elif selection == "3":
                print("You bought 1 orange at $3")
                orange_count += 1
                cost += 3

            else:
                print(f"Sorry. {selection} is an invalid option.")
                continue

        elif response == "n":
            print(Summary)
            break
    break

print(f"{apple_count} apple(s) at $2 a piece")
print(f"{grape_count} grape(s) at $1 a piece")
print(f"{orange_count} oranges at $3 a piece")
print(f"Subtotal: ${cost}")
tax = cost * .05
print(f"Tax: ${tax}")
grand_total = cost + tax
print(f"Total ${grand_total}")