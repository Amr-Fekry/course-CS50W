def square(x):
    return x * x

def main():
	for i in range(10):
		print("{} squared is {}".format(i, square(i))) # older way of format string


# only run main() if this file is being executed
if __name__ == "__main__":
	main()
# this is used to avoid running the code inside main() in other cases 
# like only trying to import a function in this file to another file 

# this also allows us to define functions below the main code
