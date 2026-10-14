
import unittest

from src.data_loader import load_data
from src.matching import (
    check_food_compatibility,
    check_capacity,
    check_location,
    check_time_compatibility,
    is_feasible,
    get_rejection_reasons
)


class TestMatching(unittest.TestCase):

    def setUp(self):
        data = load_data("data/sample_input.json")

        self.donation = data["donations"][0]
        self.recipient = data["recipients"][0]
	self.recipient["remaining_capacity"] = self.recipient["capacity"]
        self.volunteer = data["volunteers"][0]

    def test_food_compatible(self):
        self.assertTrue(
            check_food_compatibility(self.donation, self.recipient)
        )

    def test_food_incompatible(self):
        recipient = self.recipient.copy()
        recipient["accepted_food_types"] = ["Produce"]

        self.assertFalse(
            check_food_compatibility(self.donation, recipient)
        )

    def test_sufficient_capacity(self):
        self.assertTrue(
            check_capacity(self.donation, self.recipient, self.volunteer)
        )

    def test_insufficient_recipient_capacity(self):
        recipient = self.recipient.copy()
        recipient["capacity"] = 10

        self.assertFalse(
            check_capacity(self.donation, recipient, self.volunteer)
        )

    def test_insufficient_volunteer_capacity(self):
        volunteer = self.volunteer.copy()
        volunteer["vehicle_capacity"] = 10

        self.assertFalse(
            check_capacity(self.donation, self.recipient, volunteer)
        )

    def test_exact_capacity(self):
        volunteer = self.volunteer.copy()
        volunteer["vehicle_capacity"] = self.donation["quantity"]

        self.assertTrue(
            check_capacity(self.donation, self.recipient, volunteer)
        )

    def test_same_location(self):
        self.assertTrue(
            check_location(self.donation, self.recipient, self.volunteer)
        )

    def test_different_location(self):
        volunteer = self.volunteer.copy()
        volunteer["area"] = "Irvine"

        self.assertFalse(
            check_location(self.donation, self.recipient, volunteer)
        )

    def test_compatible_time(self):
        self.assertTrue(
            check_time_compatibility(
                self.donation, self.recipient, self.volunteer
            )
        )

    def test_incompatible_time(self):
        volunteer = self.volunteer.copy()
        volunteer["available_start"] = "18:00"
        volunteer["available_end"] = "20:00"

        self.assertFalse(
            check_time_compatibility(
                self.donation, self.recipient, volunteer
            )
        )

    def test_feasible_match(self):
        self.assertTrue(
            is_feasible(self.donation, self.recipient, self.volunteer)
        )

    def test_infeasible_match(self):
        recipient = self.recipient.copy()
        recipient["accepted_food_types"] = ["Produce"]

        self.assertFalse(
            is_feasible(self.donation, recipient, self.volunteer)
        )


    def test_rejection_reasons(self):
        recipient = self.recipient.copy()
        recipient["accepted_food_types"] = ["Produce"]

        reasons = get_rejection_reasons(
            self.donation,
            recipient,
            self.volunteer
        )

        self.assertIn(
            "Recipient does not accept this food type",
            reasons
        )

if __name__ == "__main__":
    unittest.main()



