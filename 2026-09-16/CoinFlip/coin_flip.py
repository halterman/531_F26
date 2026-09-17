from random import randrange

head_count = 0
tail_count = 0
number_of_tosses = 1_000_000

for _ in range(0, number_of_tosses):
    number = randrange(0, 2)
    if number == 0:
        head_count += 1
    else:
        tail_count += 1

print(f'heads: {100*head_count/number_of_tosses}%, tails: {100*tail_count/number_of_tosses}%')