option = int

print("A Simple Calculator")

print("[1] Add")
print("[2] Subtract")
print("[3] Multiply")
print("[4] Divide")
option = int(input("Choose an option."))

print(option)

if option == 1:
   print("time to add!")
elif option == 2: 
   print("time to subtract")
elif option == 3: 
    print("time to multiply")
elif option == 4: 
    print("time to divide")
else: 
   print("enter 1 or 2!")

    