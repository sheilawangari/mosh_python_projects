# The while loop will run until the user types quit

command = ""    # Set to an empty string first
while True:     # This means the user cant write with uppercase
    command = input("> ").lower()

    # if command.lower() == "start":
    #     print("The car started...")

    # elif command.lower() == "stop":
    #     print("The car stopped..")

# We dont have to repeat the 'lower' all the time, we put it at the input section

    if command == "start":
        print("The car started..")

    elif command == "stop":
        print("The car stopped..")

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
