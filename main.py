print("Welcome to my Python-Test!")
name = input("Tell me your name: ")
print("Hey,", name)

def check_name_length(name):
    if len(name) > 10:
        print("Wow, your name is quite long!")
    else:
        print("Your name has a good length.")

check_name_length(name)

while True:
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() == 'yes':
        new_name = input("Please enter a new name: ")
        check_name_length(new_name)
    else:
        print("Thank you for using this program!")
        breaklast change, text added

        breakfeature added
