user_name="ram"
password="123abcd"

user_name1=input("Enter username=")
password1=input("Enter password=")

if user_name1==user_name:
    if password1==password:
        print("Acess granted.")
else:
    print("Incorrect username and password.")