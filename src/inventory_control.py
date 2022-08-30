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
        self.ingredients = set()
        self.available_dishes = set()

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

    def ingredients_available(self):
        for item in self.min_inventory:
            if self.min_inventory[item] > 0:
                self.ingredients.add(item)

    def get_available_dishes(self):
        self.ingredients_available()
        menu = self.INGREDIENTS.items()
        for dishe, ing in menu:
            if self.ingredients.issuperset(ing):
                self.available_dishes.add(dishe)
        return self.available_dishes
