from unittest import TestCase, skip
from good import TaxableGood, NonTaxableGood
from receipt import Receipt


class TestReceipt(TestCase):

    def test_receipt_should_show_correct_amount_for_non_imported_goods(self):
        goods = [
            (1, NonTaxableGood(name="book", price=12.49, is_imported=False)),
            (1, TaxableGood(name="music CD", price=14.99, is_imported=False)),
            (1, NonTaxableGood(name="chocolate bar", price=0.85, is_imported=False))
        ]

        expected = 29.83
        result = Receipt.get_total_amount(goods)
        self.assertAlmostEqual(result, expected)

        expected = 1.5
        result = Receipt.get_total_sales_tax(goods)
        self.assertEqual(result, expected)

    def test_receipt_should_show_correct_amount_for_imported_goods(self):
        goods = [
            (1, NonTaxableGood(name="box of chocolates", price=10.0, is_imported=True)),
            (1, TaxableGood(name="bottle of perfume", price=47.50, is_imported=True))
        ]

        expected = 65.15
        result = Receipt.get_total_amount(goods)
        self.assertEqual(result, expected)

        expected = 7.65
        result = Receipt.get_total_sales_tax(goods)
        self.assertEqual(result, expected)

    def test_receipt_should_show_correct_amount_for_combination_of_goods(self):
        goods = [
            (1, TaxableGood(name="bottle of perfume", price=27.99, is_imported=True)),
            (1, TaxableGood(name="bottle of perfume", price=18.99, is_imported=False)),
            (1, NonTaxableGood(name="headache pills", price=9.75, is_imported=False)),
            (1, NonTaxableGood(name="box of chocolates", price=11.25, is_imported=True))
        ]

        expected = 74.68
        result = Receipt.get_total_amount(goods)
        self.assertAlmostEqual(result, expected)

        expected = 6.70
        result = Receipt.get_total_sales_tax(goods)
        self.assertAlmostEqual(result, expected)

    def test_receipt_should_display_no_purchase_information_if_no_goods(self):
        goods = []

        expected = ""

        result = Receipt.print(goods)

        self.assertEqual(result, expected)

    def test_receipt_should_display_purchase_information_for_1_item(self):
        goods = [(1, TaxableGood(name="bottle of perfume", price=27.99, is_imported=True))]

        expected = """1 imported bottle of perfume: 32.19
Sales Taxes: 4.20
Total: 32.19"""

        result = Receipt.print(goods)

        self.assertEqual(result, expected)

    def test_receipt_should_display_purchase_information_for_mix_of_items(self):
        goods = [
            (1, TaxableGood(name="bottle of perfume", price=27.99, is_imported=True)),
            (1, TaxableGood(name="bottle of perfume", price=18.99, is_imported=False)),
            (1, NonTaxableGood(name="packet of headache pills", price=9.75, is_imported=False)),
            (1, NonTaxableGood(name="box of chocolates", price=11.25, is_imported=True))
        ]

        expected = """1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68"""

        result = Receipt.print(goods)

        self.assertEqual(result, expected)

    def test_receipt_should_display_purchase_information_for_mix_of_items_with_different_qty(self):
        goods = [(2, TaxableGood(name="bottle of perfume", price=27.99, is_imported=True))]

        expected = """2 imported bottle of perfume: 64.38
Sales Taxes: 8.40
Total: 64.38"""

        result = Receipt.print(goods)

        self.assertEqual(result, expected)
