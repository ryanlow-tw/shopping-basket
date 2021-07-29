from abc import ABC, abstractmethod
from utils import round_up_to_nearest_five_cents


class Good(ABC):
    def __init__(self, name, price, is_imported):
        self.name = name
        self.price = price
        self.is_imported = is_imported

        if type(self) == Good:
            raise ValueError("Good class cannot be instantiated!")

    def __eq__(self, other):
        return other.name == self.name and other.price == self.price
    

class TaxableGood(Good):
    def __init__(self, name, price, is_imported):
        super().__init__(name, price, is_imported)

    def __eq__(self, other):
        return super(TaxableGood, self).__eq__(other)

    def calculate_tax(self):
        tax_rate = 0.1
        return round_up_to_nearest_five_cents(tax_rate * self.price)

class NonTaxableGood(Good):
    def __init__(self, name, price, is_imported):
        super().__init__(name, price, is_imported)

    def __eq__(self, other):
        return super(NonTaxableGood, self).__eq__(other)

    def calculate_tax(self):
        import_duty = 0.05
        return round_up_to_nearest_five_cents(import_duty * self.price) if self.is_imported else 0
