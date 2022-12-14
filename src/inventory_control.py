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
        self.__orders_list = []
        self.__consumed_ingredients = {
            ingredient: 0 for ingredient in self.MINIMUM_INVENTORY
        }

    def add_new_order(self, customer, order, day):
        available_dishes = self.get_available_dishes()

        if order not in available_dishes:
            return False

        for ingredient in self.INGREDIENTS[order]:
            if ingredient not in self.__consumed_ingredients:
                self.__consumed_ingredients[ingredient] = 1
            else:
                self.__consumed_ingredients[ingredient] += 1

        self.__orders_list.append({
            "cliente": customer,
            "pedido": order,
            "dia": day,
        })

    def get_quantities_to_buy(self):
        return self.__consumed_ingredients

    def get_available_dishes(self):
        available_dishes = set()
        remaining_ingredients = set()

        for ingredient in self.MINIMUM_INVENTORY:
            amount_minimum_inventory = self.MINIMUM_INVENTORY[ingredient]
            amount_consumed_ingredient = self.__consumed_ingredients[
                ingredient]
            if amount_minimum_inventory - amount_consumed_ingredient > 0:
                remaining_ingredients.add(ingredient)

        for dish in self.INGREDIENTS:
            if set(self.INGREDIENTS[dish]).issubset(remaining_ingredients):
                available_dishes.add(dish)

        return available_dishes
