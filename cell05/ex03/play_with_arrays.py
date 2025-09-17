array = [2, 8, 9, 48, 8, 22, -12, 2]
print(array)
new_array = []
for value in array:
    if value > 5:            
        new_array.append(value + 2)
result = set(new_array)
print(result)