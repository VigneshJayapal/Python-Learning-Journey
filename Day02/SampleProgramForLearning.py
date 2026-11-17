# Get integer input for the variable a,b,c.
# Multiple all three variables and print the result. (a*b*c)
# Add all three variables and print the result. (a+b+c)
# Divided the multiplied value by added value
# Finally print the result of the division.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
multiplied_value = a * b * c
print("The multiplied value is: ", multiplied_value)
Added_value = a + b + c
print("The added value is: ", Added_value)
Divided_value = multiplied_value / Added_value
print("The divided value is: ", Divided_value)

