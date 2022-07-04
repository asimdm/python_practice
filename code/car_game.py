print("\nRules:\n1. start- start the car\n2. stop- stop the car\n3. quit- exit the game")
comm=''
start=False
while comm.lower()!='quit':
    comm=input("\nCommand: ").lower()
    if comm=='start':
        if not start:
            print("Started the car....")
            start=True
        else:
            print("Car is already running....")
    elif comm=='stop':
        if start:
            print("The car stopped....")
            start=False
        else:
            print("Car is already not moving....")
    elif comm!='quit':
        print("I don't understand the command....")
else:
    print("You exited the game successfully")