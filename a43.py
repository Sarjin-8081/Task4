n = 28
divisors = []
for i in range(1, n):
    if n % i == 0:
        divisors.append(i)
if sum(divisors) == n:
    print("Perfect Number")
else:
    print("Not Perfect")
