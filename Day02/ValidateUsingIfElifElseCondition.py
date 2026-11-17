name = input("Enter the name: ")
condition = int(input("Enter the condition value: "))

if condition < 10:
    print("Name is: ", name)
    print("Condition is below the threshold!")
elif condition < 5:
    print("Name is: ", name)
    print("Condition is below 5!")
else:
    print("Name is: ", name)
    print("Condition is above the threshold!")
