"""
Main Implementation For Program
"""
import data_loader
import scheduler
import validation
import metrics

data = data_loader.load_data("../data/sample_input.json")

validation.validate_dataset(data)

while True:
	print("============ RESCUE ROUTE ============\n")
	print("Surplus Food Matching & Pickup Planner\n")
	print("======================================\n")

	print("a. FIFO \n")
	print("b. Greedy\n")
	print("c. Compare Both\n")
	print("d. Exit Application\n")

	menu_choices = ['a','b','c','d']

	user_input = input("Enter the menu option of your choice: \n")

	if isinstance(user_input, int) or user_input not in menu_choices:
		print("Invalid menu option\n")

	if user_input == 'a':

		fifo_assignments = scheduler.fifo_schedule(
						data["donations"],
						data["recipients"],
						data["volunteers"]
					)

		print("\n========== FIFO ASSIGNMENTS ==========\n")
		for assignment in fifo_assignments:
			print("Donation: ", assignment["donation_id"])
			print()
			print("Donations Status: ", assignment["status"])
			print()
			print("Decision Reason: ", assignment["decision_reason"])
			print("\n=====================================\n")

		print("=============== FIFO Metrics ===============\n")
		print("Donations Received: ", metrics.donations_received(data["donations"]))
		print()
		print("Donations Assigned: ", metrics.donations_assigned(fifo_assignments))
		print()
		print("Unassigned Donations: ", metrics.unassigned_donations(fifo_assignments))
		print()
		print("Food Quantity Rescued: ", metrics.food_quantity_rescued(
								fifo_assignments,
								data["donations"]
							))
		print()
		print("Food Quantity At Risk: ", metrics.food_quantity_at_risk(
								fifo_assignments,
								data["donations"]
							))
		print()
		print("Urgent Rescue Rate: ", metrics.urgent_rate_rescue(
								fifo_assignments,
								data["donations"]
							))
		print()
		print("Recipient Capacity Utilization Rate: ",
				metrics.recipient_capacity_utilization(
							fifo_assignments,
							data["donations"],
							data["recipients"]
					) 
			)
		print()

		print("Volunteer Capacity Utilization Rate: ",
				metrics.volunteer_capacity_utilization(
						fifo_assignments,
						data["donations"],
						data["volunteers"]
					)
			)
		print()
		print("===========================================")


	if user_input == 'b':

		greedy_assignments = scheduler.greedy_schedule(
						data["donations"],
						data["recipients"],
						data["volunteers"]
					)

		print("\n========== GREEDY ASSIGNMENTS ==========\n")
		for assignment in greedy_assignments:
			print("Donation: ", assignment["donation_id"])
			print()
			print("Donation Status: ", assignment["status"])
			print()
			print("Decision Reason: ", assignment["decision_reason"])
			print()
			print("\n=======================================\n")


		print("=============== Greedy Metrics ===============\n")
		print("Donations Received: ", metrics.donations_received(data["donations"]))
		print()

		print("Donations Assigned: ", metrics.donations_assigned(
							greedy_assignments
						))
		print()

		print("Unassigned Donations: ", metrics.unassigned_donations(
							greedy_assignments
						))
		print()

		print("Food Quantity Rescued: ", metrics.food_quantity_rescued(
								greedy_assignments,
								data["donations"]
							))
		print()

		print("Food Quantity At Risk: ", metrics.food_quantity_at_risk(
								greedy_assignments,
								data["donations"]
							))
		print()

		print("Urgent Rescue Rate: ", metrics.urgent_rate_rescue(
							greedy_assignments,
							data["donations"]
						), "%\n")

		print("Recipient Capacity Utilization Rate: ", metrics.recipient_capacity_utilization(
									greedy_assignments,
									data["donations"],
									data["recipients"]
								), "%\n")

		print("Volunteer Capacity Utilization Rate: ", metrics.volunteer_capacity_utilization(
									greedy_assignments,
									data["donations"],
									data["volunteers"]
								), "%\n")
		print("=============================================\n")

	if user_input == 'c':

		fifo_assignments = scheduler.fifo_schedule(
						data["donations"],
						data["recipients"],
						data["volunteers"]
					)

		greedy_assignments = scheduler.greedy_schedule(
						data["donations"],
						data["recipients"],
						data["volunteers"]
					)

		comparison = metrics.fifo_vs_greedy(
					fifo_assignments,
					greedy_assignments,
					data["donations"]
				)

		print("========== FIFO VS GREEDY COMPARISION ==========\n")
		print()
		print("Assigned Donation Difference: ", comparison["donations_assigned_difference"])
		print()
		print("Food Quantity Rescued Difference: ", comparison["rescued_difference"])
		print()
		print("Urgent Rescue Rate Difference: ", comparison["urgent_difference"])
		print()
		print("==============================================\n")

	if user_input == 'd':
		print("Thank you for using RESCUE ROUTE!")
		break














