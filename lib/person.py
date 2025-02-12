# lib/person.py

class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Testing the Person class
if __name__ == "__main__":
    alice = Person()
    alice.talk()  # Output: Hello World!
    alice.walk()  # Output: The person is walking!