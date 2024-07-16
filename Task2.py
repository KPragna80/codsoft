first = input("enter 1st number:")
second = input("enter 2nd number:")
operator = input("enter an operator ( * - + % / ) :") 

first = int(first)
second = int(second)

if operator == "*":
    print(first * second)
elif operator == "-":
    print(first - second)
elif operator == "+":
    print(first + second)        
elif operator == "%":
    print(first % second)
elif operator == "/":
    print(first / second)
else:
    print("please enter valid input")

