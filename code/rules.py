name=input("Enter name: ")
l=len(name)
if l<3:
    print("ERROR!! Name must be atleast 3 characters long")
elif l>10:
    print("ERROR!! Name can be maximum of 10 characters")
else:
    print("It's a perfect name")