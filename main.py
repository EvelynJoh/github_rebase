print("Welcome to my Python-Test!")
name = input("Tell me your name: ")
print("Hey,", name)

def check_name_length(name):
    if len(name) > 10:
        print("Wow, your name is quite long!")
    else:
        print("Your name has a good length.")

check_name_length(name)