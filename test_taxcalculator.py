from unittest import TestCase, skip
from good import Good, TaxableGood, NonTaxableGood
from tax_calculator import TaxCalculator


class TestTaxCalculator(TestCase):
    def test_calculate_tax_for_non_taxable_good(self):
        non_taxable_good = NonTaxableGood(name = "book", price = 3.3, is_imported = False)
        result = TaxCalculator.calculate_tax(non_taxable_good)
        self.assertEqual(0, result)
    
    def test_calculate_tax_for_taxable_good(self):
        taxable_good = TaxableGood(name = "perfume", price = 5, is_imported = False)
        result = TaxCalculator.calculate_tax(taxable_good)
        self.assertEqual(0.5, result)
    
    def test_calculate_tax_for_taxable_good_with_rounding_up_to_nearest_five_cents(self):
        taxable_good = TaxableGood(name = "perfume", price = 5.11, is_imported = False)
        result = TaxCalculator.calculate_tax(taxable_good)
        self.assertEqual(0.55, result)


    def test_calculate_tax_for_imported_non_taxable_good(self):
        non_taxable_good = NonTaxableGood(name = "book", price = 3, is_imported = True)
        result = TaxCalculator.calculate_tax(non_taxable_good)
        self.assertEqual(0.15, result)
    
    def test_calculate_tax_for_imported_taxable_good(self):
        taxable_good = TaxableGood(name = "perfume", price = 50, is_imported = True)
        result = TaxCalculator.calculate_tax(taxable_good)
        self.assertEqual(7.75, result)
        
        