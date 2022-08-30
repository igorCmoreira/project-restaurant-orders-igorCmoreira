from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        add_order = {
            'customer': customer,
            'order': order,
            'day': day
        }
        self.orders.append(add_order)

    def get_most_ordered_dish_per_customer(self, customer):
        order_list_cutomer = self.all_order_per_customer(customer, mode='arr')
        return Counter(order_list_cutomer).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        order_list_cutomer = self.all_order_per_customer(customer, mode='obj')
        orders = self.all_orders(mode='obj')
        never = orders - order_list_cutomer
        return never

    def get_days_never_visited_per_customer(self, customer):
        open_days = self.operating_days(mode='obj')
        visited_days = {
            order['day'] for order in self.orders
            if order['customer'] == customer
        }
        return open_days - visited_days

    def get_busiest_day(self):
        open_days = self.operating_days(mode='arr')
        return Counter(open_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        open_days = self.operating_days(mode='arr')
        return Counter(open_days).most_common()[-1][0]

    def all_order_per_customer(self, customer, mode):
        if mode == 'obj':
            return {
                order['order'] for order in self.orders
                if order['customer'] == customer
            }
        return [
                order['order'] for order in self.orders
                if order['customer'] == customer
            ]

    def all_orders(self, mode):
        if mode == 'obj':
            return {
                order['order'] for order in self.orders
            }
        return [
                order['order'] for order in self.orders
            ]

    def operating_days(self, mode):
        if mode == 'obj':
            return {
                order['day'] for order in self.orders
            }
        return [
                order['day'] for order in self.orders
            ]
