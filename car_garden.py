from os import system

garden = [
    "v",
    ".",
    "v",
    "v",
    ".",
    ".",
    ".",
    "v",
    ".",
    ".",
]


# render
while True:
    system("cls")
    print ()

    for pi in range(len(garden)):
        print(garden[pi], end="")

    print()
    print()

    # stats
    count = 0
    for pi in range(len(garden)):
        if garden [pi] == "v":
            count += 1

    plants = count * 100 / len(garden)
    print(f"plants:{plants:3.2f}% ")
    print()

    print("ACTIONS\n",)
    menu = {
        "actions": [
            "Plant",
            "Gather",
            "Replant",
            "Exit"
            ]
            }
    for menu_num in range(len(menu["actions"])):
        print(menu_num + 1, menu["actions"][menu_num])

    action = int(input(">"))

    # ACTION SELECTION
    ##################################################### 1
    if action == 1:
        while True:
            idx = int(input("Where?: "))
            idx -= 1
            if idx < len(garden):
                if garden[idx] == ".":
                    garden[idx] = "v"
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
            if idx < len(garden):
                if garden[idx] == "v":
                    garden[idx] = "."
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
            if idx > len(garden):
                print("Do not steal fron vecinului place!")
                continue
            elif garden[idx] == ".":
                print("Nothing to replant!")
                continue

            idx2 = int(input("To where?: "))
            idx2 -= 1
            if idx2 > len(garden):
                print("Do you want to make a gift for vecinu!")
                continue
            if garden[idx2] == "v":
                print("Place already planted, try another place!")
                continue

            if idx and idx2 < len(garden):
                if garden[idx] == "v" and garden[idx2] == ".":
                    garden[idx] = "."
                    garden[idx2] = "v"
                    break

    #####################################################4
    if action == 4:
        system("cls")
        print("Exit")
        break
