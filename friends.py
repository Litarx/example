from os import system

friends = []
while True:
    system("cls")
    print(len(friends))
    for list in friends:
        print(list)
    enter = input("Do you want to add or remove friend? (a/r): ")
    if enter == "a":
        add_friend = input("Add Name: ")
        friends.append(add_friend)
    elif enter == "r":
        add_friend = input("Do you want to be alone?(y/n): ")
        if add_friend == "y":
            friends.clear()
            print(f"You have now {len(friends)} fiends" )
            break
    else:
        pass
