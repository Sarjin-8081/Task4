user_string=input("Enter a string=")

num_digits=0
letters=0
space=0

for i in user_string:
    if i.isdigit():
        num_digits+=1
    elif i.isalpha():
        letters+=1
    elif i.isspace():
        space+=1

print("Digits=",num_digits)
print("Letters=",letters)
print("Space=",space)