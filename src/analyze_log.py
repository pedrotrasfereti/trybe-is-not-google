from csv import DictReader


def read_csv_file(path):
    try:
        with open(path, "r") as file:
            data = DictReader(file, ["cliente", "pedido", "dia"])

            return list(data)

    except FileNotFoundError:
        raise FileNotFoundError("File not found!")


def write_to_file(path, content):
    with open(path, "w") as file:
        file.write(content)


def get_most_ordered_item_by_customer(data, customer):
    orders = []

    for row in data:
        curr_customer = row["cliente"]
        curr_order = row["pedido"]

        if curr_customer == customer:
            orders.append(curr_order)

    most_ordered = max(set(orders), key=orders.count)

    return most_ordered


def get_total_burger_ordered_by_customer(data, customer):
    hamburgers = 0

    for row in data:
        curr_customer = row["cliente"]
        curr_order = row["pedido"]

        if curr_customer == customer and curr_order == "hamburguer":
            hamburgers += 1

    return hamburgers


def analyze_log(path_to_file):
    raise NotImplementedError
