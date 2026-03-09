odd_numbers = []
count = 0
while count < 2:
    for i in range(101):
        if i % 2 != 0:
            odd_numbers.append(i)
            count += 1
print(odd_numbers)

