# product.py

class Product:
    def __init__(self, cost_of_materials, discount_on_products, cost_of_shipping, insurance_added, discount_percentage, quantity):
        self.cost_of_materials = cost_of_materials
        self.discount_on_products = discount_on_products / 100
        self.cost_of_shipping = cost_of_shipping
        self.insurance_added = insurance_added
        self.discount_percentage = discount_percentage / 100
        self.quantity = quantity

    def calculate_discounted_cost(self):
        return self.cost_of_materials * (1 - self.discount_on_products)

    def calculate_customs_duties(self, discounted_cost):
        return 0.45 * (discounted_cost + self.cost_of_shipping)

    def calculate_total_cost(self, discounted_cost, customs_duties):
        return discounted_cost + self.cost_of_shipping + customs_duties

    def calculate_markup(self, total_cost):
        return total_cost * 0.15

    def calculate_original_selling_price(self, total_cost, markup):
        return total_cost + markup + self.insurance_added

    def calculate_final_selling_price(self, original_selling_price):
        return original_selling_price * (1 - self.discount_percentage)

    def calculate_total_final_price(self, final_selling_price):
        return final_selling_price * self.quantity
