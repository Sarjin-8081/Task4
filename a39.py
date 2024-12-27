even_sum = 0
odd_sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n
print("Even:", even_sum, "Odd:", odd_sum)
