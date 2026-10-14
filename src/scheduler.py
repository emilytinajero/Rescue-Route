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

	for recipient in recipients:
		recipient["remaining_capacity"] = recipient["capacity"]

	for volunteer in volunteers:
		volunteer["current_pickups"] = 0

	for donation in donations:
		recipient, volunteer = find_first_match(
							donation,
							recipients,
							volunteers
					)

		if recipient is not None:

			decision_reason = (
				f"Donation {donation['donation_id']} was assigned "
				f"to {recipient['organization_name']} with volunteer "
				f"{volunteer['volunteer_id']} because it was the "
				f"first feasible recipient-volunteer match found under FIFO scheduling."
			)

			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : recipient["recipient_id"],
					"volunteer_id" : volunteer["volunteer_id"],
					"scheduled_time" : donation["ready_time"],
					"decision_reason" : decision_reason,
					"status" : "assigned"
			}
			# need to update the volunteers max pickups and recipients capacity
			volunteer["current_pickups"] += 1
			recipient["remaining_capacity"] -= donation["quantity"]

		else:
			rejection_reasons = []

			for recipient in recipients:
				for volunteer in volunteers:

					rejection_reasons.extend( matching.get_rejection_reasons(donation, recipient, volunteer))
			decision_reason = "; ".join(set(rejection_reasons))

		
			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : None,
					"volunteer_id" : None,
					"scheduled_time" : None,
					"decision_reason" : decision_reason, # replace with rejection reason from matching.py later
					"status" : "unassigned"
			}
		
		assignments.append(assignment)

	return assignments


"""
Greedy schedule algorithim
Chooses based on closest expiration
"""
def greedy_schedule(donations, recipients, volunteers):

	assignments = []

	for recipient in recipients:
		recipient["remaining_capacity"] = recipient["capacity"]

	for volunteer in volunteers:
		volunteer["current_pickups"] = 0

	sorted_donations = sorted(donations, key=lambda donation : donation["expiry_time"])

	for donation in sorted_donations:
		recipient, volunteer = find_first_match(
						donation,
						recipients,
						volunteers
		)

		if recipient is not None:

			decision_reason = (
					f"Donation {donation['donation_id']} was assigned to "
					f"{recipient['organization_name']} with "
					f"volunteer {volunteer['volunteer_id']} because "
					f"it had the earliest expiration time among remaining donations"
					f"under the greedy urgency-first strategy. {recipient['organization_name']} "
					f"accepts {donation['food_type']}, "
					f"had sufficient capacity available, and volunteer {volunteer['volunteer_id']} "
				        f"could transport the donation quantity."
			)

			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : recipient["recipient_id"],
					"volunteer_id" : volunteer["volunteer_id"],
					"scheduled_time" : donation["ready_time"],
					"decision_reason" : decision_reason,
					"status" : "assigned"
			}

			volunteer["current_pickups"] += 1
			recipient["remaining_capacity"] -= donation["quantity"]

		else:
			assignment = {
					"donation_id" : donation["donation_id"],
					"recipient_id" : None,
					"volunteer_id" : None,
					"scheduled_time" : None,
					"decision_reason" : "something about being deferred",
					"status" : "unassigned"
			}

		assignments.append(assignment)

	return assignments

