import json
from datetime import datetime


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
		# validates the donation id
		if info["donation_id"] != key:
			print("Invalid donation id: ", key)
			valid = False
		# validates the donation quantity
		if info["quantity"] <= 0:
			print("Invalid quantity for donation: ", key)
			valid = False
		# validates that there is a pickup area
		if not info["pickup_area"]:
			print(f"No pickup area was specified for donation: {key}.\n")
			valid = False
		# validates that there is a food type
		if not info["food_type"]:
			print(f"No valid food type provided for donations {key}.\n")
			valid = False
		# validates expiry was provided
		if not info["expiry"]:
			print(f"No expiration for donation {key} was provided\n")
			valid = False
		# validates that a ready time was provided
		if not info["ready_time"]:
			print("No ready time was provided for donation: ", key)
			print()
			valid = False
		# validates ready time was provided in the correct format
		try:
			datetime.strptime(info["ready_time"], "%H:%M")

		except ValueError:
			print(f"The provided ready time for donation {key} is formatted incorrectly.\n")
			valid = False
	return valid

# Function to validate Recipients

def validate_recipients(recipients):
	valid = True
	for key, info in recipients.items():

		# validates recipient id provided
		if info["recipient_id"] != key:
			print("Invalid recipient id: ", key)
			valid = False
		# validates capacity is more than 0
		if info["capacity"] <= 0:
			print(f"Recipient {key} has no capacity\n")
			valid = False
		# validates food type was provided
		if not info["accepted_food_types"]:
			print(f"No accepted food types specified for recipient {key}.\n")
			valid = False
		# validates location was provided
		if not info["location"]:
			print(f"No location specified for recipient {key}.\n")
			valid = False
		# validates closing time was provided
		if not info["closing_time"]:
			print(f"Not closing time specified for recipient {key}\n")
			valid = False
		# validates closing time is in correct format
		try:
			datetime.strptime(info["closing_time"], "%H:%M")

		except ValueError:
			print(f"The provided closing time for recipient {key} is formatted incorrectly.\n")
			valid = False
	return valid

# Function to validate volunteers

def validate_volunteers(volunteers):
	valid = True
	for key, info in volunteers.items():

		# validates volunteer id
		if info["volunteer_id"] != key:
			print("Invalid volunteer id: ", key)
			valid = False
		# validates vehicle cap provided
		if not info["vehicle_cap"]:
			print(f"No vehicle cap was provided for volunteer {key}.\n")
			valid = False
		# validates max pickups provided
		if not info["max_pickups"]:
			print(f"Max pickups not provided for volunteer {key}.\n")
			valid = False
		#validates location is provided
		if not info["location"]:
			print(f"Location not provided for volunteer {key}.\n")
			valid = False
		# validates start availability is provided
		if not info["availability_start"]:
			print(f"No starting availability provided for volunteer {key}.\n")
			valid = False
		# validates end availability time is provided
		if not info["availability_end"]:
			print(f"No ending availability provided for volunteer {key}.\n")
			valid = False
		# validates start time format
		try:
			datetime.strptime(info[availability_start], "%H:%M")

		except ValueError:
			print(f"Availability start time not formatted correctly for volunteer {key}\n")
			valid = False
		# validates end time format
		try:
			datetime.strptime(info[availability_end], "%H:%M")

		except ValueError:
			print(f"Availability end time not formatted correctly for volunteer {key}.")
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






