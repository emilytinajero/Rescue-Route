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
	for donation in donations:
		if donation_id in donations["id"]:
			print("Donation id exists: ", donation_id)
			return False

		if quantity in donations["quantity"] < 0:
			print("There is nothing left: ", quantity)
			return False
		#eventually put validation check for ready time
	return True



# Import all data structures/data from main.py
# This file will be used to define all necessary functions




# OBJECTIVES

# Validate IDs, quantities, food types, capacities, availability, time values

# Function for identifying feasible donation-recipient-volunteer matches

#Implement FIFO baseline (queue)

# Implmenet greedy strategy (i.e. food with nearest expiration date)

#






