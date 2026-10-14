"""
Module that calculates all required metrics and returns them
"""

from datetime import datetime

"""
Function to calculate donations recieved
"""
def donations_recieved(donations):
	return len(donations)

"""
Function to calculate donations assigned
"""
def donations_assigned(assignments):
	count = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			count += 1

	return count

"""
Function to calculate unassigned donations
"""
def unassigned_donations(assignments):
	count = 0

	for assignment in assignments:
		if assignment["status"] == "unassigned":
			count += 1

	return count

"""
Function to calculate total quantity successfully assigned
"""
def food_quantity_rescued(assignments, donations)
	count = 0

	for assignment in assignments:
		if assignment["status"] == "assigned":
			count += donations["quantity"]

	return count
