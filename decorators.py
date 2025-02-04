def announce(f):
    def wrapper():
        print("function is startinmg ....\n")
        f()
        print("\nfunction is end!")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()