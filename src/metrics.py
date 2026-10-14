"""
Module that calculates all required metrics and returns them
"""

from datetime import datetime
import lookup
import data_loader
import scheduler

"""
Function to calculate donations recieved
"""
def donations_received(donations):
	return len(donations)

"""
Function to calculate donations assigned
"""
def donations_assigned(assignments):
	assigned_donations = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			assigned_donations += 1

	return assigned_donations

"""
Function to calculate unassigned donations
"""
def unassigned_donations(assignments):
	donations_unassigned = 0

	for assignment in assignments:
		if assignment["status"] == "unassigned":
			donations_unassigned += 1

	return donations_unassigned

"""
Function to calculate total quantity successfully assigned
"""
def food_quantity_rescued(assignments, donations):
	rescued_food = 0

	donation_id_lookup = lookup.create_donation_lookup(donations)

	for assignment in assignments:
		if assignment["status"] == "assigned":
			donation_id = assignment["donation_id"]
			rescued_food += (donation_id_lookup[donation_id]["quantity"])

	return rescued_food

"""
Function to calculate food quantity at risk
"""
def food_quantity_at_risk(assignments, donations):
	food_at_risk = 0

	donation_id_lookup = lookup.create_donation_lookup(donations)

	for assignment in assignments:
		if assignment["status"] == "unassigned":
			donation_id = assignment["donation_id"]
			food_at_risk += (donation_id_lookup[donation_id]["quantity"])

	return food_at_risk

"""
Function for urgent rescue rate
"""


"""
Function for recipient capacity utilization
"""
def recipient_capacity_utilization(assignments, donations, recipients):
	total_recipient_capacity = 0

	for recipient in recipients:
		total_recipient_capacity += recipient["capacity"]

	donation_id_lookup = lookup.create_donation_lookup(donations)

	assigned_quantity = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			donation_id = assignment["donation_id"]
			assigned_quantity += (donation_id_lookup[donation_id]["quantity"])

	return (assigned_quantity / total_recipient_capacity) * 100

"""
Function to calculate volunteer capacity utlization
"""
def volunteer_capacity_utilization(assignments, donations, volunteers):
	total_volunteer_capacity = 0

	for volunteer in volunteers:
		total_volunteer_capacity += volunteer["vehicle_capacity"]

	donation_id_lookup = lookup.create_donation_lookup(donations)
	assigned_quantity = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			donation_id = assignment["donation_id"]
			assigned_quantity += (donation_id_lookup[donation_id]["quantity"])

	return (assigned_quantity / total_volunteer_capacity) * 100

"""
test code
"""

data = data_loader.load_data("../data/sample_input.json")

print("\n==============================")
print("FIFO SCHEDULER TEST")
print("===============================")

print("FIFO donations loaded:", len(data["donations"]))
print()
fifo_assignments = scheduler.fifo_schedule(data["donations"], data["recipients"], data["volunteers"])

print("\nFIFO Metrics")
print()
print("Donations Received: ", donations_received(data["donations"]))
print()
print("Donations Assigned: ", donations_assigned(fifo_assignments))

print()
print("Donations Unassigned: ", unassigned_donations(fifo_assignments))
print()

print("Food Quantity Rescued: ", food_quantity_rescued(fifo_assignments, data["donations"]))
print()

print("Recipient Capacity Utilization: ", recipient_capacity_utilization(fifo_assignments, data["donations"], data["recipients"]), "%")
print()


print("\n========================")
print("GREEDY SCHEDULER TEST")
print("=========================")

data = data_loader.load_data("../data/sample_input.json")

print("Greedy donations loaded: ", len(data["donations"]))
print()
greedy_assignments = scheduler.greedy_schedule(data["donations"], data["recipients"], data["volunteers"])

print("\nGreedy Metrics")
print()
print("Donations Received: ", donations_received(data["donations"]))
print()

print("Donations Assigned: ", donations_assigned(greedy_assignments))
print()

print("Donations Unassigned: ", unassigned_donations(greedy_assignments))

print("Food Quantity Rescued: ", food_quantity_rescued(greedy_assignments, data["donations"]))
print()

print("Food Quantity at Risk: ", food_quantity_at_risk(greedy_assignments, data["donations"]))
print()

print("Recipient Capacity Utilization: ", volunteer_capacity_utilization(greedy_assignments, data["donations"], data["volunteers"]), "%")


