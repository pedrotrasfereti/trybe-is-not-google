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
    all_orders = []

    for row in data:
        if row["cliente"] == customer:
            all_orders.append(row["pedido"])

    most_ordered = max(set(all_orders), key=all_orders.count)

    return most_ordered


def analyze_log(path_to_file):
    raise NotImplementedError
