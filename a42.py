s = "programming"
vowels = "aeiou"
result = ""
for c in s:
    if c not in vowels:
        result += c
print(result)
