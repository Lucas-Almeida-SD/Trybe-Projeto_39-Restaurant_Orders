import csv

FILE_NOT_FOUND = 'FILE_NOT_FOUND'
INVALID_EXTENSION = 'INVALID_EXTENSION'


def get_orders_list(path_to_file: str):
    file_extension = path_to_file.split('.')[-1]

    if file_extension != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            reader = list(csv.reader(file))

        orders_list = []
        header = ["cliente", "pedido", "dia"]

        for info in reader:
            orders_list.append(dict(zip(header, info)))

        return orders_list
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def get_dish_most_ordered_by_maria(orders_list):
    dishes = dict()
    dish_most_ordered = orders_list[0]['pedido']
    amount_dish_most_ordered = 0

    for order in orders_list:
        if order['cliente'] == 'maria':
            pedido = order['pedido']

            if pedido not in dishes:
                dishes[pedido] = 1
            else:
                dishes[pedido] += 1

            if dishes[pedido] > amount_dish_most_ordered:
                dish_most_ordered = pedido
                amount_dish_most_ordered = dishes[pedido]

    return dish_most_ordered


def analyze_log(path_to_file):
    orders_list = get_orders_list(path_to_file)

    dish_most_ordered_by_maria = get_dish_most_ordered_by_maria(orders_list)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(f"{dish_most_ordered_by_maria}\n")
