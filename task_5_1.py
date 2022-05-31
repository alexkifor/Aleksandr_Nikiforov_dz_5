def num_generation(n):
    for i in range(1, n + 1, 2):
        yield (i)

num_gen = num_generation(13)
for num in num_gen:
    print(num)
