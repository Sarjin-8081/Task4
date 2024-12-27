lst = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(1, 11):
    for num in lst:
        print(f"{i} x {num} = {num * i}")
    print()  # Print a blank line after each iteration for readability
