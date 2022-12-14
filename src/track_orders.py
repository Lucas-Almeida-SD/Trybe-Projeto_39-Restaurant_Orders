class TrackOrders:
    def __init__(self):
        self.__orders_list = []

    def __len__(self):
        return len(self.__orders_list)

    def add_new_order(self, customer, order, day):
        self.__orders_list.append({
            "cliente": customer,
            "pedido": order,
            "dia": day,
        })

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = dict()
        orders_list = self.__orders_list
        dish_most_ordered = orders_list[0]['pedido']
        amount_dish_most_ordered = 0

        for order in orders_list:
            if order['cliente'] == customer:
                pedido = order['pedido']

                if pedido not in dishes:
                    dishes[pedido] = 1
                else:
                    dishes[pedido] += 1

                if dishes[pedido] > amount_dish_most_ordered:
                    dish_most_ordered = pedido
                    amount_dish_most_ordered = dishes[pedido]

        return dish_most_ordered

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
