age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old")
years = 0
for i in range(0,3):
    years += 10
    age += 10
    print(f"In {years} years, you will be {age} years old")