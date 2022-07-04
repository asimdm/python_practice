from random import randint, random


secret_no=randint(1,10)
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    no=int(input("\nYour guess: "))
    if no==secret_no:
        print("Congrats!!! You guessed the number!")
        break
    else:
        print("Wrong guess :(")
    guess_count+=1
else:
    print(f"\nOh No  :(  You ran out of chances....\nThe secret number was {secret_no}")