import json

def load_data(filename):
	with open(filename, "r") as file:
		data = json.load(file)

	donations = data["donations"]
	recipients = data["recipients"]
	volunteers = data["volunteers"]

	return donations, recipients, volunteers

# Function to validate all attributes of donations dictionary

def validate_donations(donations):
	valid = True
	for key, info in donations.items():

		if info["donation_id"] != key:
			print("Invalid donation id: ", key)
			valid = False

		if info["quantity"] <= 0:
			print("Invalid quantity for: ", key)
			valid = False

	return valid



# Import all data structures/data from main.py
# This file will be used to define all necessary functions




# OBJECTIVES

# Validate IDs, quantities, food types, capacities, availability, time values

# Function for identifying feasible donation-recipient-volunteer matches

#Implement FIFO baseline (queue)

# Implmenet greedy strategy (i.e. food with nearest expiration date)

#






