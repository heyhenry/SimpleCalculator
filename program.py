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

    print("")
    print("A Simple Calculator")
    print("")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("")
    option = int(input("Choose an option: "))

    if option == 1:
        
        print("")
        print("Mode: Addition")
        print("-----")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = firstNumber + secondNumber
        print("")
        print("Result: " + str(result))
        print("-----")
        print("")
        
        while running: 

            print("[1] Return to Menu")
            print("[2] Exit Program")
            print("")
            confirmation = int(input("Choose an option: "))

            # returns user to menu
            if confirmation == 1:
                break
            # exits program
            elif confirmation == 2:
                running = False
            # repeats question due to invalid input
            else: 
                print("")
                print("Invalid Input! Enter a valid choice.")
                print("")
    
    elif option == 2: 
        
        print("")
        print("Mode: Subtraction")
        print("-----")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = firstNumber - secondNumber
        print("")
        print("Result: " + str(result))
        print("-----")
        print("")

        while running: 

            print("[1] Return to Menu")
            print("[2] Exit Program")
            print("")
            confirmation = int(input("Choose an option: "))

            # returns user to menu
            if confirmation == 1:
                break
            # exits program
            elif confirmation == 2:
                running = False
            # repeats question due to invalid input
            else: 
                print("")
                print("Invalid Input! Enter a valid choice.")
                print("")
    
    elif option == 3: 
        
        print("")
        print("Mode: Multiplication")
        print("-----")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = firstNumber * secondNumber
        print("")
        print("Result: " + str(result))
        print("-----")
        print("")

        while running: 

            print("[1] Return to Menu")
            print("[2] Exit Program")
            print("")
            confirmation = int(input("Choose an option: "))

            # returns user to menu
            if confirmation == 1:
                break
            # exits program
            elif confirmation == 2:
                running = False
            # repeats question due to invalid input
            else: 
                print("")
                print("Invalid Input! Enter a valid choice.")
                print("")
    
    elif option == 4: 
        
        print("")
        print("Mode: Division")
        print("-----")
        firstNumber = int(input("Enter first number: "))
        secondNumber = int(input("Enter second number: "))
        result = firstNumber / secondNumber
        print("")
        print("Result: " + str(result))
        print("-----")
        print("")

        while running: 

            print("[1] Return to Menu")
            print("[2] Exit Program")
            print("")
            confirmation = int(input("Choose an option: "))

            # returns user to menu
            if confirmation == 1:
                break
            # exits program
            elif confirmation == 2:
                running = False
            # repeats question due to invalid input
            else: 
                print("")
                print("Invalid Input! Enter a valid choice.")
                print("")
    
    else: 
        
        print("")
        print("Invalid Input! Enter a valid choice.")
        continue






    