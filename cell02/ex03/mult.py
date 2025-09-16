num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
result = num1 * num2
if result > 0:
    check = "positive"
elif result < 0:
    check = "negative"
else:
    check = "positive and negative"
print(f"{num1} * {num2} = {result}\nThe result is {check}.")