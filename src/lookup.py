"""
Module for lookup helper functions
"""
def donation_lookup(donations):
	donation_lookup = {}

	for donation in donations:
		donation_lookup[donation["donation_id"]] = donation
	return donation_lookup

def recipient_lookup(recipients):
	recipient_lookup = {}

	for recipient in recipients:
		recipient_lookup[recipient["recipient_id"]] = recipient

	return recipient_lookup

def volunteer_lookup(volunteers):
	volunteer_lookup = {}

	for volunteer in volunteers:
		volunteer_lookup[volunteer["volunteer_id"]] = volunteer

	return volunteer_lookup



