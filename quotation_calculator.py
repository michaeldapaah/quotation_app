# quotation_calculator.py

from product import Product

class QuotationCalculator:
    def __init__(self):
        self.products = []
        self.total_final_price = 0.0

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, index):
        if index < len(self.products):
            self.products.pop(index)

    def calculate_total(self, bank_transfer_cost, customs_agency_fees):
        self.total_final_price = 0.0
        for product in self.products:
            discounted_cost = product.calculate_discounted_cost()
            customs_duties = product.calculate_customs_duties(discounted_cost)
            total_cost = product.calculate_total_cost(discounted_cost, customs_duties)
            markup = product.calculate_markup(total_cost)
            original_selling_price = product.calculate_original_selling_price(total_cost, markup)
            final_selling_price = product.calculate_final_selling_price(original_selling_price)
            self.total_final_price += product.calculate_total_final_price(final_selling_price)
        
        self.total_final_price += bank_transfer_cost + customs_agency_fees
        return self.total_final_price
