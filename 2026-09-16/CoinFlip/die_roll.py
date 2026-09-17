from random import randrange


counts = [0 for _ in range(6)]
number_of_rolls = 10_000_000

for _ in range(0, number_of_rolls):
    roll = randrange(6)   # 0, 1, 2, 3, 4, or 5
    counts[roll] += 1

print(f'1/6 = {1/6}')
for i in range(6):
    print(f'{i + 1}: {100*counts[i]/number_of_rolls}')
