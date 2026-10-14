
from datetime import datetime


def check_food_compatibility(donation, recipient):
    """Check whether the recipient accepts the donated food."""
    return donation["food_type"] in recipient["accepted_food_types"]


def check_capacity(donation, recipient, volunteer):
    """Check whether the recipient and volunteer have enough capacity."""
    quantity = donation["quantity"]

    return (
        quantity <= recipient["remaining_capacity"]
        and quantity <= volunteer["vehicle_capacity"]
    )


def check_location(donation, recipient, volunteer):
    """Check whether all three records belong to the same area."""
    return (
        donation["pickup_area"] == recipient["area"]
        and donation["pickup_area"] == volunteer["area"]
    )


def check_time_compatibility(donation, recipient, volunteer):
    """Check whether there is a shared pickup and delivery window."""

    fmt = "%H:%M"

    ready = datetime.strptime(donation["ready_time"], fmt)
    expiry = datetime.strptime(donation["expiry_time"], fmt)
    closing = datetime.strptime(recipient["closing_time"], fmt)

    start = datetime.strptime(volunteer["available_start"], fmt)
    end = datetime.strptime(volunteer["available_end"], fmt)

    earliest = max(ready, start)
    latest = min(expiry, closing, end)

    return earliest < latest


def is_feasible(donation, recipient, volunteer):
    """Determine whether an assignment satisfies all basic constraints."""

    return (
        check_food_compatibility(donation, recipient)
        and check_capacity(donation, recipient, volunteer)
        and check_location(donation, recipient, volunteer)
        and check_time_compatibility(donation, recipient, volunteer)
        and check_volunteer_pickups(volunteer)
    )




def get_rejection_reasons(donation, recipient, volunteer):
    """
    Return a list of reasons why a match is infeasible.
    An empty list means all basic compatibility checks passed.
    """

    reasons = []

    if not check_food_compatibility(donation, recipient):
        reasons.append("Recipient does not accept this food type")

    if not check_capacity(donation, recipient, volunteer):
        reasons.append("Insufficient recipient or volunteer capacity")

    if not check_location(donation, recipient, volunteer):
        reasons.append("Donation, recipient, and volunteer areas do not match")

    if not check_time_compatibility(donation, recipient, volunteer):
        reasons.append("No overlapping time window")


    if not check_volunteer_pickups(volunteer):
        reasons.append(
            f"Volunteer {volunteer['volunteer_id']} has reached "
            f"the maximum of {volunteer['max_pickups']} pickups"
        )
    return reasons

def check_volunteer_pickups(volunteer):
    current_pickups = volunteer.get("current_pickups", 0)
    max_pickups = volunteer["max_pickups"]

    return current_pickups < max_pickups 


def get_defered_message(donation, priority_donation):
    """
    Explain why a donation was considered after another
    donation under the greedy scheduling strategy.
    """

    donation_id = donation["donation_id"]
    priority_id = priority_donation["donation_id"]

    return (
        f"Donation {donation_id} was considered after "
        f"Donation {priority_id} because {priority_id} "
        f"had higher priority under the urgency-first "
        f"greedy scheduling rule."
    )

