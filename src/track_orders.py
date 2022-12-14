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
        orders_list = self.__orders_list
        dishes = dict()
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
        orders_list = self.__orders_list
        dishes = set()
        customer_dishes = set()

        for order in orders_list:
            dishes.add(order['pedido'])
            if order['cliente'] == customer:
                customer_dishes.add(order['pedido'])

        return dishes.difference(customer_dishes)

    def get_days_never_visited_per_customer(self, customer):
        orders_list = self.__orders_list
        days = set()
        customer_days = set()

        for order in orders_list:
            days.add(order['dia'])
            if order['cliente'] == customer:
                customer_days.add(order['dia'])

        return days.difference(customer_days)

    def get_busiest_day(self):
        orders_list = self.__orders_list
        days = dict()
        busiest_day = ''
        amount_busiest_day = 0

        for order in orders_list:
            day = order['dia']

            if day not in days:
                days[day] = 1
            else:
                days[day] += 1

            if days[day] > amount_busiest_day:
                busiest_day = day
                amount_busiest_day = days[day]

        return busiest_day

    def get_least_busy_day(self):
        orders_list = self.__orders_list
        days = dict()
        least_busy_day = ''
        amount_least_busy_day = len(self)

        for order in orders_list:
            day = order['dia']

            if day not in days:
                days[day] = 1
            else:
                days[day] += 1

            if days[day] <= amount_least_busy_day:
                least_busy_day = day
                amount_least_busy_day = days[day]

        return least_busy_day
