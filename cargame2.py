# The while loop will run until the user types quit

command = ""    # Set to an empty string first
started = False
while True:     # This means the user cant write with uppercase
    command = input("> ").lower()

    # if command.lower() == "start":
    #     print("The car started...")

    # elif command.lower() == "stop":
    #     print("The car stopped..")

# We dont have to repeat the 'lower' all the time, we put it at the input section

    if command == "start":
        if started:
            print("Car is already started!")

        else:
            started = True
            print("Car started..")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")

        else:
            started = False
            print("Car stopped..")   
        
    elif command == "help":     # When using multiline comments everything is captured inside including indentation
        print("""
start - to start the car
stop - to stop the car         
quit - to quit
        """)

    elif command == "quit":
        break

    else:
        print("Sorry I dont understand that!")
