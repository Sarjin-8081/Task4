nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)
