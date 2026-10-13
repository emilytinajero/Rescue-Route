from datetime import datetime 


def validate_time(time_string):
    if not isinstance(time_string, str):
        raise ValueError("Time must be a string")

    try:
        datetime.strptime(time_string, "%H:%M")
    except ValueError:
        raise ValueError(f"Invalid time: {time_string}")

    return True 


 
def validate_donation(donation):

    required_fields = [
        "donation_id",
        "donor_name",
        "food_type",
        "quantity",
        "pickup_area",
        "ready_time",
        "expiry_time"
    ]

    # 1. Check that every required field exists
    for field in required_fields:
        if field not in donation:
            raise ValueError(f"Missing required field: {field}")

    # 2. Validate text fields
    for field in [
        "donation_id",
        "donor_name",
        "food_type",
        "pickup_area"
    ]:
        if not isinstance(donation[field], str) or not donation[field].strip():
            raise ValueError(f"Invalid {field}")

    # 3. Validate quantity
    if type(donation["quantity"]) is not int or donation["quantity"] <= 0:
        raise ValueError("Donation quantity must be a positive integer")

    # 4. Validate times
    validate_time(donation["ready_time"])
    validate_time(donation["expiry_time"])

    ready = datetime.strptime(donation["ready_time"], "%H:%M")
    expiry = datetime.strptime(donation["expiry_time"], "%H:%M")

    if expiry <= ready:
        raise ValueError("Expiry must be after ready time")

    return True

    

def validate_recipient(recipient):

    required_fields = [
        "recipient_id",
        "organization_name",
        "accepted_food_types",
        "capacity",
        "area",
        "closing_time"
    ]


    # Check that all required fields exist
    for field in required_fields:
        if field not in recipient:
            raise ValueError(f"Missing recipient field: {field}")

    # Validate text fields
    for field in ["recipient_id", "organization_name", "area"]:
        if not isinstance(recipient[field], str) or not recipient[field].strip():
            raise ValueError(f"Invalid recipient field: {field}")

    # Validate accepted food types
    food_types = recipient["accepted_food_types"]

    if not isinstance(food_types, list) or not food_types:
        raise ValueError("Accepted food types must be a nonempty list")

    for food_type in food_types:
        if not isinstance(food_type, str) or not food_type.strip():
            raise ValueError("Invalid accepted food type")

    # Validate capacity
    if type(recipient["capacity"]) is not int or recipient["capacity"] <= 0:
        raise ValueError("Recipient capacity must be a positive integer")

    # Validate closing time
    validate_time(recipient["closing_time"])

    return True



def validate_volunteer(volunteer):

    required_fields = [
        "volunteer_id",
        "vehicle_capacity",
        "area",
        "available_start",
        "available_end",
        "max_pickups"
    ]

    # Check required fields
    for field in required_fields:
        if field not in volunteer:
            raise ValueError(f"Missing volunteer field: {field}")

    # Validate volunteer ID and area
    for field in ["volunteer_id", "area"]:
        if not isinstance(volunteer[field], str) or not volunteer[field].strip():
            raise ValueError(f"Invalid volunteer field: {field}")

    # Validate vehicle capacity
    if type(volunteer["vehicle_capacity"]) is not int or volunteer["vehicle_capacity"] <= 0:
        raise ValueError("Vehicle capacity must be a positive integer")

    # Validate maximum pickups
    if type(volunteer["max_pickups"]) is not int or volunteer["max_pickups"] <= 0:
        raise ValueError("Maximum pickups must be a positive integer")

    # Validate availability times
    validate_time(volunteer["available_start"])
    validate_time(volunteer["available_end"])

    start = datetime.strptime(volunteer["available_start"], "%H:%M")
    end = datetime.strptime(volunteer["available_end"], "%H:%M")

    if end <= start:
        raise ValueError("Volunteer availability end must be after start")

    return True




def validate_unique_ids(records, id_field):
    """
    Verify that every record has a unique ID.
    """

    seen_ids = set()

    for record in records:
        if id_field not in record:
            raise ValueError(f"Missing ID field: {id_field}")

        record_id = record[id_field]

        if not isinstance(record_id, str) or not record_id.strip():
            raise ValueError(f"Invalid ID: {record_id}")

        if record_id in seen_ids:
            raise ValueError(f"Duplicate ID found: {record_id}")

        seen_ids.add(record_id)

    return True




def validate_dataset(data):
    """
    Validate all donations, recipients, and volunteers.
    """

    for category in ["donations", "recipients", "volunteers"]:
        if category not in data or not isinstance(data[category], list):
            raise ValueError(f"Missing or invalid category: {category}")

    for donation in data["donations"]:
        validate_donation(donation)

    for recipient in data["recipients"]:
        validate_recipient(recipient)

    for volunteer in data["volunteers"]:
        validate_volunteer(volunteer)

    validate_unique_ids(data["donations"], "donation_id")
    validate_unique_ids(data["recipients"], "recipient_id")
    validate_unique_ids(data["volunteers"], "volunteer_id")

    return True
