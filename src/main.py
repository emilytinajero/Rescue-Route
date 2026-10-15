"""
Main Implementation For Program
"""

"""
TODO:
- print out some sort of title screen/intro thingy
- prompt user for input on whether they want to see fifo or greedy
- if fifo:
	* load data
	* call validate data function from validation.py
	* create fifo_assignments by calling fifo_schedule()
	* print out the metrics in a pretty organized way using funcs
	from the metrics.py

- if greedy:
	* load data
	* vall validate data functiion from validation.py
	* create greedy_assignments by calling fifo_schedule()
	* print out metrics in pretty organized way

- print comparision in pretty way
"""
import data_loader
import matching
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

		print("\n=============== FIFO Metrics ===============\n")
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

	if user_input == 'd':
		print("Thank you for using RESCUE ROUTE!")
		break
