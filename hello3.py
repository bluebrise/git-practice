user_input = input("Enter some names separated by commas: ")
names = [name.strip() for name in user_input.split(",")]
    
print("You entered the following names:")
for name in names:
    print(name)