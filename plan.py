for i in range(0,5):
    print(i)


l=[1,4,3,5]
for i in enumerate(l):
    print(i)


password = ""

while password != "secret":
    password = input("Enter the password: ")
    if password == "secret":
        print("access granted")
    else:
        print("access denied")