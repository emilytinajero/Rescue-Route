
from datetime import datetime


def check_food_compatibility(donation, recipient):
    """Check whether the recipient accepts the donated food."""
    return donation["food_type"] in recipient["accepted_food_types"]


def check_capacity(donation, recipient, volunteer):
    """Check whether the recipient and volunteer have enough capacity."""
    quantity = donation["quantity"]

    return (
        quantity <= recipient["capacity"]
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

    return reasons