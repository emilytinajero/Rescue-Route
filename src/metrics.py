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
def urgent_rate_rescue(assignments, donations):

	sorted_donations = sorted(donations, key=lambda donation : donation["expiry_time"])
	urgent_count = max(1, len(donations) // 4)

	urgent_donations = sorted_donations[:urgent_count]

	urgent_ids = set()

	for donation in urgent_donations:
		urgent_ids.add(donation["donation_id"])

	assigned_urgent = 0

	for assignment in assignments:
		if (assignment["status"] == "assigned" and assignment["donation_id"] in urgent_ids):
			assigned_urgent += 1

	return (assigned_urgent / urgent_count) * 100

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
Function to calculate FIFO vs Greedy Comparison
"""
def fifo_vs_greedy(fifo_assignments, greedy_assignments, donations):
	donations_assigned_difference = (
		donations_assigned(greedy_assignments) - donations_assigned(fifo_assignments)
	)

	rescued_difference = (

		food_quantity_rescued(greedy_assignments, donations) - food_quantity_rescued(fifo_assignments, donations)
	)

	urgent_difference = (
		urgent_rate_rescue(greedy_assignments, donations) - urgent_rate_rescue(fifo_assignments, donations)
	)

	return {
		"donations_assigned_difference" : donations_assigned_difference,
		"rescued_difference" : rescued_difference,
		"urgent_difference" : urgent_difference
	}
