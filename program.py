# option = 0

# print("A Simple Calculator")

# print("[1] Add")
# print("[2] Subtract")
# print("[3] Multiply")
# print("[4] Divide")
# option = int(input("Choose an option."))

# if option == 1:
#    print("time to add!")
# elif option == 2: 
#    print("time to subtract")
# elif option == 3: 
#     print("time to multiply")
# elif option == 4: 
#     print("time to divide")
# else: 
#    print("enter 1 or 2!")

running = True

while running:

    print("A Simple Calculator")

    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    
    option = int(input("Choose an option."))

    if option == 1:
        print("time to add!")
        print("")
        while running: 

            confirmation = input("Would you like to go back to [m] menu or [e] exit?")
            # returns user to menu
            if confirmation == "m":
                break
            # exits program
            elif confirmation == "e":
                running = False
            # repeats question due to invalid input
            else: 
                print("Invalid Input! Enter valid choice.")
                print("")
    
    elif option == 2: 
        print("time to subtract")
    
    elif option == 3: 
        print("time to multiply")
    
    elif option == 4: 
        print("time to divide")
    
    else: 
        print("ty come again")
        break






    