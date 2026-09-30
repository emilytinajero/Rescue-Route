import functions


donations = {}
recipients = {}
volunteers = {}

def main():
	global donations
	global recipients
	global volunteers
	
	donations, recipients, volunteers = ( functions.load_data("input.json"))

	print(donations)
	print(recipients)
	print(volunteers)
	print()
	
	if functions.validate_donations(donations):
		print("Donations are valid")
	else:
		print("Donation validation failed")


if __name__ == "__main__":
	main()



# This file will be used to implement the demo program

# define dictionary for id lookup

# define set for food-type compatability

# define list/deque for FIFO baseline

# def assignment history as a list

# define metrics as a dictonary



