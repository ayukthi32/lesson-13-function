#activity2\
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("SElect your operation")
print(" a .Addition")
print(" b . Subtraction")
print (" c. Multiplication")
print(" d. Division")

choice = input("Enter your choice a/b/c/d")

num_1 = int(input("enter number 01"))
num_2 = int(input("Enter number 02"))

if choice== 'a':
    print( num_1, "+" , num_2 , "=" , add(num_1 , num_2) )

elif choice == "b":
    print(num_1 , "-" , num_2 , "=" , subtract(num_1 , num_2))

elif choice == "c":
    print(num_1 , "*" , num_2 , "=" , multiply(num_1 , num_2))

elif choice == "d":
    print(num_1 , "/" , num_2 , "=" , divide(num_1 , num_2))

else:
    print("This is invalid")  
