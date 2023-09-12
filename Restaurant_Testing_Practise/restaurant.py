class Table:
    # constructor
    def __init__(self, people):
        self.bill = []
        self.people = people


    def order(self, item, price, quantity):
        order_details = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(order_details)
        return self.bill

    def order_no_quantity(self, item, price):
        for x in range(len(self.bill)):
            if self.bill[x]['item'] == item and self.bill[x]['price'] == price:
                self.bill[x]['quantity'] += 1
                return self.bill

    def remove(self, item, price, quantity):
        if len(self.bill) == 0:
            return False
        for x in range(len(self.bill)):
            if self.bill[x]['item'] == item and self.bill[x]['price'] == price:
                self.bill[x]['quantity'] -= quantity
                if self.bill[x]['quantity'] < 0:
                    self.bill[x]['quantity'] += quantity
                    return False
                elif self.bill[x]['quantity'] == 0:
                    self.bill.pop(x)
                    return True
                else:
                    return True


    def get_subtotal(self):
        subtotal = 0
        for order in self.bill:
            subtotal += order["price"] * order["quantity"]
            subtotal = round(subtotal, 2)
        return subtotal

    def get_total(self, charge):
        service = charge * Table.get_subtotal(self)
        service = round(service, 2)
        final = service + Table.get_subtotal(self)
        final = round(final, 2)
        total = {"Sub Total": f"£{Table.get_subtotal(self)}", "Service Charge": f"£{service}", "Total": f"£{final}"}
        return total

    def split_bill(self):
        split_bill = 0
        split_bill = Table.get_subtotal(self)/ self.people
        split_bill = round(split_bill/ 2)
        return split_bill

