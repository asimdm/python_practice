weight=int(input("Enter your weight: "))
form=input("which format is the weight in? (L)bs/(K)g: ")
if form=='l' or form=='L':
    con_weight=weight*0.45
    print("The weight in Kilograms is {0} Kgs".format(con_weight))
elif form=='K' or form=='k':
    con_weight=weight/0.45
    print("The weight in Pounds is {0} Lbs".format(con_weight))
else:
    print("Wrong entry")
