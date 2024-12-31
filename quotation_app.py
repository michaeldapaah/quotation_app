# quotation_app.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from product import Product
from quotation_calculator import QuotationCalculator

class QuotationApp:
    def __init__(self, root):
        self.calculator = QuotationCalculator()
        self.create_widgets(root)

    def create_widgets(self, root):
        # Create input fields and labels
        ttk.Label(root, text="Cost of Materials:").grid(column=0, row=0, padx=10, pady=5)
        self.entry_cost_of_materials = ttk.Entry(root)
        self.entry_cost_of_materials.grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(root, text="Discount on Products (%):").grid(column=0, row=1, padx=10, pady=5)
        self.entry_discount_on_products = ttk.Entry(root)
        self.entry_discount_on_products.grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(root, text="Cost of Shipping:").grid(column=0, row=2, padx=10, pady=5)
        self.entry_cost_of_shipping = ttk.Entry(root)
        self.entry_cost_of_shipping.grid(column=1, row=2, padx=10, pady=5)

        ttk.Label(root, text="Insurance Added:").grid(column=0, row=3, padx=10, pady=5)
        self.entry_insurance_added = ttk.Entry(root)
        self.entry_insurance_added.grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(root, text="Discount (%):").grid(column=0, row=4, padx=10, pady=5)
        self.entry_discount_percentage = ttk.Entry(root)
        self.entry_discount_percentage.grid(column=1, row=4, padx=10, pady=5)

        ttk.Label(root, text="Bank Transfer Cost:").grid(column=0, row=5, padx=10, pady=5)
        self.entry_bank_transfer_cost = ttk.Entry(root)
        self.entry_bank_transfer_cost.grid(column=1, row=5, padx=10, pady=5)

        ttk.Label(root, text="Customs Agency Fees:").grid(column=0, row=6, padx=10, pady=5)
        self.entry_customs_agency_fees = ttk.Entry(root)
        self.entry_customs_agency_fees.grid(column=1, row=6, padx=10, pady=5)

        ttk.Label(root, text="Quantity:").grid(column=0, row=7, padx=10, pady=5)
        self.entry_quantity = ttk.Entry(root)
        self.entry_quantity.grid(column=1, row=7, padx=10, pady=5)

        # Button to add the product
        ttk.Button(root, text="Add Product", command=self.add_product).grid(column=0, row=8, columnspan=2, pady=10)

        # Table to display products
        self.columns = ("Cost of Materials", "Discount on Products (%)", "Cost of Shipping", "Customs Duties (%)", "Insurance Added", "Discount (%)", "Quantity")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.tree.heading(col, text=col)
        self.tree.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

        # Button to remove the selected product
        ttk.Button(root, text="Remove Product", command=self.remove_product).grid(column=0, row=10, columnspan=2, pady=10)

        # Button to calculate the total result
        ttk.Button(root, text="Calculate Total", command=self.calculate_total).grid(column=0, row=11, columnspan=2, pady=10)

        # Label to display the result
        self.result_var = tk.StringVar()
        ttk.Label(root, textvariable=self.result_var).grid(column=0, row=12, columnspan=2, pady=10)

    def add_product(self):
        try:
            product = Product(
                float(self.entry_cost_of_materials.get()),
                float(self.entry_discount_on_products.get()),
                float(self.entry_cost_of_shipping.get()),
                float(self.entry_insurance_added.get()),
                float(self.entry_discount_percentage.get()),
                int(self.entry_quantity.get())
            )
            self.calculator.add_product(product)
            
            # Add product details to the table
            self.tree.insert("", tk.END, values=(
                product.cost_of_materials,
                product.discount_on_products * 100,
                product.cost_of_shipping,
                0,  # Placeholder for calculated customs duties
                product.insurance_added,
                product.discount_percentage * 100,
                product.quantity
            ))
            
            messagebox.showinfo("Product Added", f"Product {len(self.calculator.products)} added successfully.")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def clear_entries(self):
        self.entry_cost_of_materials.delete(0, tk.END)
        self.entry_discount_on_products.delete(0, tk.END)
        self.entry_cost_of_shipping.delete(0, tk.END)
        self.entry_insurance_added.delete(0, tk.END)
        self.entry_discount_percentage.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def remove_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Get index of the selected item
            item_index = self.tree.index(selected_item[0])
            # Remove from products list
            self.calculator.remove_product(item_index)
            # Remove from the table
            self.tree.delete(selected_item)
            messagebox.showinfo("Product Removed", "Selected product has been removed.")
        else:
            messagebox.showerror("Selection Error", "Please select a product to remove.")

    def calculate_total(self):
        try:
            bank_transfer_cost = float(self.entry_bank_transfer_cost.get())
            customs_agency_fees = float(self.entry_customs_agency_fees.get())

            total_final_price = self.calculator.calculate_total(bank_transfer_cost, customs_agency_fees)

            # Display results
            self.result_var.set(f"Total Final Selling Price: {total_final_price:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("Quotation Calculator")

# Initialize the app
app = QuotationApp(root)

# Run the main event loop
root.mainloop()