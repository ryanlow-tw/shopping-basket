from unittest import TestCase
from utils import round_up_to_nearest_five_cents


class TestUtils(TestCase):
    def test_round_up_to_nearest_five_cents_should_not_change_whole_numbers(self):
        self.assertEqual(5, round_up_to_nearest_five_cents(5))

    def test_round_up_to_nearest_five_cents(self):
        self.assertAlmostEqual(5.05, round_up_to_nearest_five_cents(5.01))
