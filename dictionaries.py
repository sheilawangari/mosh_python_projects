# Keys and values are associated
# Each key is associated with a value

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

# When you use 'get' to find a value or key it will not bring an error rather it will show a 'None'
print(customer.get("birthdate"))

print(customer.get("birthdate", "Jan 1 1980"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}


output = ""
for ch in phone:  # We get each character and then use it to access a key value pair in our dictionary
    output += digits_mapping.get(ch, "!") + " "  # When the user gets to put a character thats not part of our dict, 
                                  # the program will not yell at them
print(output)                                   # If we dont have that key, our program will provide an "!"
                                   # In each iteration we get to add to the output string