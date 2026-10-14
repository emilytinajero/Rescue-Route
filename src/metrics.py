"""
Module that calculates all required metrics and returns them
"""

from datetime import datetime

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

	for assignment in assignments:
		if assignment["status"] == "assigned":
			rescued_food += donations["quantity"]

	return rescued_food

"""
Function to calculate food quantity at risk
"""
def food_quantity_at_risk(assignments, donations):
	food_at_risk = 0

	for assignment in assignments:
		if assignment["status"] == "unassigned":
			food_at_risk += donations["quantity"]

	return food_at_risk

"""
Function for urgent rescue rate
"""


"""
Function for recipient capacity utilization
"""
def recipient_capacity_utilization(assignments, donations):
	recipient_capacity_utilization = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			recipient_capacity_utilization += donations["quantity"]
			recipient_capacity_utilization = recipient_capacity_utilization / recipients["capacity"]

	return recipient_capacity_utilization

"""
Function to calculate volunteer capacity utlization
"""
def volunteer_capacity_utilization(assignments, donations):
	volunteer_capacity_utilization = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			volunteer_capacity_utilization += donations["quantity"]
			volunteer_capacity_utilization = volunteer_capacity_utilization / volunteers["capacity"]

	return volunteer_capacity_utilization
