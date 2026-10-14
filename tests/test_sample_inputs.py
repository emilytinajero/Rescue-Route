"""
Tests driven by the sample JSON files in data/.

- invalid_inputs.json: every case must be rejected by validate_dataset
  with the expected error message.
- empty_input.json: empty lists are valid input.
- sample_input.json: each scenario donation hits the matching outcome
  it was designed for.
"""

import unittest

from src.data_loader import load_data
from src.validation import validate_dataset
from src.matching import is_feasible, get_rejection_reasons


class TestInvalidInputs(unittest.TestCase):

    def setUp(self):
        self.cases = load_data("data/invalid_inputs.json")["cases"]

    def test_every_invalid_case_is_rejected(self):
        for case in self.cases:
            with self.subTest(case=case["name"]):
                with self.assertRaises(ValueError) as ctx:
                    validate_dataset(case["data"])
                self.assertIn(case["expected_error"], str(ctx.exception))


class TestEmptyInput(unittest.TestCase):

    def test_empty_lists_are_valid(self):
        data = load_data("data/empty_input.json")
        self.assertTrue(validate_dataset(data))
        self.assertEqual(len(data["donations"]), 0)


class TestSampleScenarios(unittest.TestCase):

    def setUp(self):
        self.data = load_data("data/sample_input.json")
        self.donations = {d["donation_id"]: d for d in self.data["donations"]}
        self.recipients = {r["recipient_id"]: r for r in self.data["recipients"]}
        self.volunteers = {v["volunteer_id"]: v for v in self.data["volunteers"]}

    def any_feasible(self, donation_id):
        donation = self.donations[donation_id]
        return any(
            is_feasible(donation, r, v)
            for r in self.recipients.values()
            for v in self.volunteers.values()
        )

    def reasons_for(self, donation_id):
        """Every rejection reason seen across all recipient/volunteer pairs."""
        donation = self.donations[donation_id]
        reasons = set()
        for r in self.recipients.values():
            for v in self.volunteers.values():
                reasons.update(get_rejection_reasons(donation, r, v))
        return reasons

    def test_sample_file_is_valid(self):
        self.assertTrue(validate_dataset(self.data))

    def test_normal_match(self):
        self.assertTrue(is_feasible(
            self.donations["D001"], self.recipients["R001"], self.volunteers["V001"]
        ))

    def test_no_recipient_accepts_food_type(self):
        # D003 Baked Goods in Fullerton; Fullerton shelter only takes Prepared Meals
        self.assertFalse(self.any_feasible("D003"))
        self.assertEqual(
            get_rejection_reasons(
                self.donations["D003"], self.recipients["R001"], self.volunteers["V001"]
            ),
            ["Recipient does not accept this food type"],
        )

    def test_insufficient_recipient_capacity(self):
        # D004 is 80 units; V003's truck holds 100 but R001 only holds 50
        self.assertFalse(is_feasible(
            self.donations["D004"], self.recipients["R001"], self.volunteers["V003"]
        ))

    def test_no_volunteer_with_enough_vehicle_capacity(self):
        # D005 is 40 units; R003 holds 60 but V004 only carries 25
        self.assertFalse(self.any_feasible("D005"))
        self.assertIn("Insufficient recipient or volunteer capacity",
                      self.reasons_for("D005"))

    def test_near_expiry_still_feasible(self):
        # D011 only has a 15-minute window but it fits inside R001/V001 hours
        self.assertTrue(is_feasible(
            self.donations["D011"], self.recipients["R001"], self.volunteers["V001"]
        ))

    def test_no_overlapping_time_window(self):
        # D012 is ready at 19:30 after the shelter closes and volunteers leave
        self.assertFalse(self.any_feasible("D012"))
        self.assertIn("No overlapping time window", self.reasons_for("D012"))

    def test_no_recipient_or_volunteer_in_area(self):
        self.assertFalse(self.any_feasible("D013"))
        self.assertIn("Donation, recipient, and volunteer areas do not match",
                      self.reasons_for("D013"))

    def test_competing_donations_each_fit_alone_but_not_together(self):
        # D006 and D007 (25 each) both fit R004 alone, but R004 holds only 30
        recipient = self.recipients["R004"]
        volunteer = self.volunteers["V005"]
        d6, d7 = self.donations["D006"], self.donations["D007"]
        self.assertTrue(is_feasible(d6, recipient, volunteer))
        self.assertTrue(is_feasible(d7, recipient, volunteer))
        self.assertGreater(d6["quantity"] + d7["quantity"], recipient["capacity"])


if __name__ == "__main__":
    unittest.main()
