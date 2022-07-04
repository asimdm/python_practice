price=1000000
credit=input("Is the buyer's credit good?(yes/no): ")
if credit=='yes':
    pay=10*price/100
else:
    pay=20*price/100
print("The downpayment is ",pay)