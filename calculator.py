import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, y):
    return math.pow(x, y)

print("Scientific Calculator")
print("1. Square Root (√x)")
print("2. Factorial (x!)")
print("3. Natural Log (ln(x))")
print("4. Power (xʸ)")

choice = int(input("Enter choice: "))
if choice in [1, 2, 3, 4]:
    num = float(input("Enter number: "))
    if choice == 1:
        print("Result:", square_root(num))
    elif choice == 2:
        print("Result:", factorial(int(num)))
    elif choice == 3:
        print("Result:", natural_log(num))
    elif choice == 4:
        num2 = float(input("Enter exponent: "))
        print("Result:", power(num, num2))
else:
    print("Invalid choice")
