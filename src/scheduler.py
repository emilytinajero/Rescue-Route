"""
FIFO and Greedy scheduling algorithms
"""
import matching

def find_first_match(donation, recipients, volunteers):
	for recipient in recipients:
		for volunteer in volunteers:
			matching.is_feasible(donation,recipient,volunteer)
			return recipient, volunteer

	return None

