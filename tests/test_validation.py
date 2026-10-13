
import unittest

from src.data_loader import load_data
from src.validation import (
    validate_donation,
    validate_recipient,
    validate_volunteer,
    validate_unique_ids,
    validate_dataset
)


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.data = load_data("data/sample_input.json")

    def test_valid_donation(self):
        donation = self.data["donations"][0]
        self.assertTrue(validate_donation(donation))

    def test_negative_quantity(self):
        donation = self.data["donations"][0].copy()
        donation["quantity"] = -10

        with self.assertRaises(ValueError):
            validate_donation(donation)

    def test_missing_donation_field(self):
        donation = self.data["donations"][0].copy()
        del donation["food_type"]

        with self.assertRaises(ValueError):
            validate_donation(donation)

    def test_invalid_donation_time(self):
        donation = self.data["donations"][0].copy()
        donation["ready_time"] = "25:00"

        with self.assertRaises(ValueError):
            validate_donation(donation)

    def test_valid_recipient(self):
        recipient = self.data["recipients"][0]
        self.assertTrue(validate_recipient(recipient))

    def test_invalid_recipient_capacity(self):
        recipient = self.data["recipients"][0].copy()
        recipient["capacity"] = 0

        with self.assertRaises(ValueError):
            validate_recipient(recipient)

    def test_valid_volunteer(self):
        volunteer = self.data["volunteers"][0]
        self.assertTrue(validate_volunteer(volunteer))

    def test_invalid_volunteer_capacity(self):
        volunteer = self.data["volunteers"][0].copy()
        volunteer["vehicle_capacity"] = -5

        with self.assertRaises(ValueError):
            validate_volunteer(volunteer)

    def test_duplicate_donation_ids(self):
        donations = [
            {"donation_id": "D001"},
            {"donation_id": "D001"}
        ]

        with self.assertRaises(ValueError):
            validate_unique_ids(donations, "donation_id")

    def test_valid_dataset(self):
        self.assertTrue(validate_dataset(self.data))


if __name__ == "__main__":
    unittest.main()
