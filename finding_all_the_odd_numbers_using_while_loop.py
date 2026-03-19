every_odd_numbers = []
count = 0
while count < 2:
    for i in range(101):
        if i % 2 != 0:
            every_odd_numbers.append(i)
            count += 1
print(every_odd_numbers)

