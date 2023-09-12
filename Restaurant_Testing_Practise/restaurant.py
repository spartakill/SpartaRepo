class Table:
    # constructor
    def __init__(self, people):
        self.bill = []
        self.people = people


    def order(self, item, price, quantity=1):
        ordered_item = False
        for x in self.bill: # x refers to an existing item
            if item == x["item"] and price == x["price"]:
                x["quantity"] += quantity
                ordered_item = True
        if not ordered_item:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

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
        return subtotal

    def get_total(self, charge = 0.1):
        service = charge * Table.get_subtotal(self)
        final = service + Table.get_subtotal(self)
        total = {"Sub Total": f"£{'{:.2f}'.format(Table.get_subtotal(self))}", "Service Charge": f"£{'{:.2f}'.format(service)}", "Total": f"£{'{:.2f}'.format(final)}"}
        return total

    def split_bill(self):
        split_bill = 0
        split_bill = self.get_subtotal()/self.people
        split_bill = float("{:.2f}".format(split_bill))
        return split_bill


