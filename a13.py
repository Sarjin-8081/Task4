lst = [1, 2, 3, "d", 4, 5, "a"]

for i in lst:
    if type(i) == int:  
        print("Numeric Data type =", i)
    elif type(i) == str:  
        print("Alphabet Data type =", i)
