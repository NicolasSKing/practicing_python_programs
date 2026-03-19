all_the_numbers_not_ending_at_zero_or_five = []
for i in range(101):
    if i % 10 != 0 and i % 5 != 0:
        all_the_numbers_not_ending_at_zero_or_five.append(i)
print(all_the_numbers_not_ending_at_zero_or_five)

