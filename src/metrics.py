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
