numbers = [5, 2, 5, 2, 2]    # We iterate over every item on this list
for x_count in numbers:    # x_count is the number Xs in each line
    # print('x' * x_count)     # This is the shortest way to do it
    # Lets use inner loop to solve this question
    output = ''      # We have set our variable into an empty string
    for count in range(x_count):   # We need to add 5 Xs to this string so we use a loop 
        output += 'x'      # We append an X to our output variable
    print(output)