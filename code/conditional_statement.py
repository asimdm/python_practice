hot=input("Is it hot today?(yes/no) ")
if hot=='yes':
    is_hot=True
else:
    is_hot=False
if is_hot:
    print("It's a hot day!!")
    print("Drink plenty of water")
else:
    cold=input("Is it cold today?(yes/no) ")
    if cold=='yes':
        is_cold=True
    else:
        is_cold=False
    if is_cold:
        print("It's a cold day!!")
        print("Wear warm clothes")
    else:
        print("It's a lovely day!!!!")