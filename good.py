from abc import ABC


class Good(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

        if type(self) == Good:
            raise ValueError("Good class cannot be instantiated!")


    def __eq__(self, other):
        return other.name == self.name and other.price == self.price


class TaxableGood(Good):

    def __init__(self, name, price):
        super().__init__(name, price)

    def __eq__(self, other):
        return super(TaxableGood, self).__eq__(other)


class NonTaxableGood(Good):

    def __init__(self, name, price):
        super().__init__(name, price)

    def __eq__(self, other):
        return super(NonTaxableGood, self).__eq__(other)
