from unittest import TestCase
from good import Good, TaxableGood, NonTaxableGood


class TestGood(TestCase):

    def test_that_good_cannot_be_instantiated(self):
        with self.assertRaises(ValueError) as ve:
            Good("perfume", 34.34)

        self.assertEqual(str(ve.exception), "Good class cannot be instantiated!")


class TestTaxableGood(TestCase):
    def setUp(self):
        name = "perfume"
        price = 34.34
        self.good = TaxableGood(name, price)

    def test_good_has_essential_attributes(self):
        self.assertIsNotNone(self.good)

        self.assertEqual(self.good, TaxableGood("perfume", 34.34))


class TestNonTaxableGood(TestCase):
    def setUp(self):
        name = "book"
        price = 34.34
        self.good = NonTaxableGood(name, price)

    def test_good_has_essential_attributes(self):
        self.assertIsNotNone(self.good)

        self.assertEqual(self.good, NonTaxableGood("book", 34.34))
