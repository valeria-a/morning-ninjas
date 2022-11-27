class Customer:
    def __init__(self, name, address, phone, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"<Customer>\n" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Phone: {self.phone}"

    def __repr__(self):
        return f"<Customer> {self.name}"

# c = Customer('adv', 'sdfs', 'sdfs')
# c.phone = '054-342342'

#
# d1 = {
#     'address':'sdfs'
# }
#
# c1 = Customer()

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.customers: dict[str: Customer] = {}
        # customers
        # inventory
        # order_product
        # orders
        # shipments

    def add_customer(self, name, address, phone, email=None):
        new_customer = Customer(name, address, phone, email)
        self.customers[name] = new_customer

    def add_product_to_inventory(self):
        pass

    def add_qty(self):
        pass

    def get_out_of_stock(self):
        pass

    def add_order(self):
        pass

