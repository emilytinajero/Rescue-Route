"""
FIFO and Greedy scheduling algorithms
"""
import matching
import data_loader

def find_first_match(donation, recipients, volunteers):

	"""
	  Returns the first feasible recipient-volunteer pair
	"""
	for recipient in recipients:
		for volunteer in volunteers:
			if matching.is_feasible(donation,recipient,volunteer):
				return recipient, volunteer

	return None, None

"""
Function to create assignment if match found
Create Rejection Record if match not found
"""
def fifo_schedule(donations, recipients, volunteers):

	assignments = []

	for volunteer in volunteers:
		volunteer["current_pickups"] = 0

	for donation in donations:
		recipient, volunteer = find_first_match(
							donation,
							recipients,
							volunteers
					)

		if recipient is not None:
			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : recipient["recipient_id"],
					"volunteer_id" : volunteer["volunteer_id"],
					"status" : "assigned"
			}
			# need to update the volunteers max pickups and recipients capacity
			volunteer["current_pickups"] += 1
			recipient["capacity"] -= donation["quantity"]

		else:
			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : None,
					"volunteer_id" : None,
					"status" : "unassigned"
			}
		assignments.append(assignment)

	return assignments




