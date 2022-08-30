from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.min_inventory = dict(self.MINIMUM_INVENTORY)
        self.list_orders = TrackOrders()

    def add_new_order(self, customer, order, day):
        self.list_orders.add_new_order(customer, order, day)
        ingredients = self.INGREDIENTS[order]
        for item in ingredients:
            if not self.min_inventory[item]:
                return False
            self.min_inventory[item] -= 1

    def get_quantities_to_buy(self):
        return {
            item: (
                self.MINIMUM_INVENTORY[item] - self.min_inventory[item]
            ) for item in self.min_inventory
        }
