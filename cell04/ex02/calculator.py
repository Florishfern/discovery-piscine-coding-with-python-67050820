num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

operator = ["+", "-", "/", "*"]

for op in operator:
    expression = f"{num1}{op}{num2}"
    result = int(eval(expression))   
    print(f"{num1} {op} {num2} = {result}")
