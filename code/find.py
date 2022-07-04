numbers=list(map(int,input("Please enter numbers: ").split()))
n=int(input("Enter number to find: "))
if n in numbers:
    print(f"Found at {numbers.index(n)+1}")
else:
    print("Not found!!")