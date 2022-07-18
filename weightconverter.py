weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')   # the input function always returns a string

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")

else:
    converted = weight / 0.45    # the slash gives a floating number while a double slash // gives an integer
    print(f"You are {converted} pounds")