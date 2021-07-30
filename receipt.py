from utils import round_to_two_decimal_places


class Receipt:

    @staticmethod
    def get_total_amount(goods):
        return sum([qty * good.calculate_price_with_tax() for qty, good in goods])

    @staticmethod
    def get_total_sales_tax(goods):
        return sum([qty * good.calculate_tax() for qty, good in goods])

    @staticmethod
    def print(goods):

        if not goods:
            return ""

        receipt_text = ""

        for qty, good in goods:
            import_status = "imported " if good.is_imported else ""
            total_price_of_good = good.calculate_price_with_tax()
            receipt_text += f"{qty} {import_status}{good.name}: {round_to_two_decimal_places(qty * total_price_of_good)}\n"

        total_tax = Receipt.get_total_sales_tax(goods)
        receipt_text += f"Sales Taxes: {round_to_two_decimal_places(total_tax)}\n"
        total_price = Receipt.get_total_amount(goods)
        receipt_text += f"Total: {round_to_two_decimal_places(total_price)}"

        return receipt_text
