list=[1,2,3,4,"a","b"]

numeric=[]
string_lst=[]

for i in list:
    if type(i)==int:
        numeric.append(i)
    elif type(i)==str:
        string_lst.append(i)
print("Numeric list=",numeric)
print("String list=",string_lst)