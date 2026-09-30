import json

def load_data(filename):
	with open(filename, "r") as file:
		data = json.load(file)
	
	donations = data["donations"]
	recipients = data["recipients"]
	volunteers = data["volunteers"]

	return donations, recipients, volunteers

# Function to check for duplicate IDs

def add_donation_id(donation_id):
	if donation_id in donations:
		print("Duplicate ticket id: ", donation_id)
		return False
	donations["donation_id"].add(donation_id)
	return True


# Import all data structures/data from main.py
# This file will be used to define all necessary functions




# OBJECTIVES

# Validate IDs, quantities, food types, capacities, availability, time values

# Function for identifying feasible donation-recipient-volunteer matches

#Implement FIFO baseline (queue)

# Implmenet greedy strategy (i.e. food with nearest expiration date)

#






