from os import system

# parking2d = parking
# pi = place index
# ri = row index

parking = [
    ["🚘", "🆓", "🆓", "🆓", "🆓"],
    ["🆓", "🚘", "🚘", "🆓", "🚘"],
    ["🚘", "🆓", "🚘", "🆓", "🚘"],
    ["🆓", "🚘", "🆓", "🚘", "🆓"],
]


# render
while True:
    system("cls")
    for ri in range(len(parking)):
        for pi in range(len(parking[ri])):
            print("|",parking[ri][pi], sep="",end=" |")
        print()  
        print("-----" * len(parking[ri]))
    print("")
    print()


##################   CONTINUE FIX FROM HERE    ######################    
    # stats
    count = 0
    for pi in range(len(parking)):
        if parking[pi] == "v":
            count += 1

    plants = count * 100 / len(parking)
    print(f"plants:{plants:3.2f}% ")
    print()

    print(
        "ACTIONS\n",
    )
    menu = {"actions": ["Plant", "Gather", "Replant", "Exit"]}
    for menu_num in range(len(menu["actions"])):
        print(menu_num + 1, menu["actions"][menu_num])

    action = int(input(">"))

    # ACTION SELECTION
    ##################################################### 1
    if action == 1:
        while True:
            idx = int(input("Where?: "))
            idx -= 1
            if idx < len(parking):
                if parking[idx] == ".":
                    parking[idx] = "v"
                    break
                else:
                    print("Place already planted, try another place")
            else:
                print("Do not plant la vecinu!")
    ##################################################### 2
    if action == 2:
        while True:
            idx = int(input("From where?: "))
            idx -= 1
            if idx < len(parking):
                if parking[idx] == "v":
                    parking[idx] = "."
                    break
                else:
                    print("Nothing to gather!")
            else:
                print("Its vecinului place")
    ##################################################### 3
    if action == 3:
        while True:
            idx = int(input("From where?: "))
            idx -= 1
            if idx > len(parking):
                print("Do not steal fron vecinului place!")
                continue
            elif parking[idx] == ".":
                print("Nothing to replant!")
                continue

            idx2 = int(input("To where?: "))
            idx2 -= 1
            if idx2 > len(parking):
                print("Do you want to make a gift for vecinu!")
                continue
            if parking[idx2] == "v":
                print("Place already planted, try another place!")
                continue

            if idx and idx2 < len(parking):
                if parking[idx] == "v" and parking[idx2] == ".":
                    parking[idx] = "."
                    parking[idx2] = "v"
                    break

    #####################################################4
    if action == 4:
        system("cls")
        print("Exit")
        break
