greeting = "hello splinter"
print(greeting)

def welcome_message():
    global greeting
    greeting = "Hello human"
    print(greeting)
    return(greeting)

welcome_message()
print(f"New greeting = {greeting}")




