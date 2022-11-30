class Shipment:

    STATUSES = ('processing', 'shipped', 'delivered')
    counter = 0

    def __init__(self, address):
        self.address = address
        self.status = 0
        Shipment.counter += 1

    def change_status_to_next(self) -> bool:
        if self.status == len(Shipment.STATUSES) - 1:
            print('Bad status')
            return False
        self.status += 1
        return True


class Order:
    pass

    # customer
    # list of products
    # get_total_price()