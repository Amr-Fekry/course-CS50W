# creating an object of the class and accessing its properties

class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():

    # Create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)
    # if you know the order of the class parameters, you don't need to specify the names and can pass the values directly in the right order.
    # if you don't, you can specify the names and pass them in any order

    # Change the value of a variable.
    f.duration += 10

    # Print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__ == "__main__":
    main()

# only when this file is run NOT imported by other file, run main()
