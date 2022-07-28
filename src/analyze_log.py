from csv import DictReader


# csv file helpers
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


# data helpers
def get_most_ordered_item_by_customer(data, customer):
    orders = []

    for row in data:
        curr_customer = row["cliente"]
        curr_order = row["pedido"]

        if curr_customer == customer:
            orders.append(curr_order)

    most_ordered = max(set(orders), key=orders.count)

    return most_ordered


def get_total_burgers_ordered_by_customer(data, customer):
    hamburgers = 0

    for row in data:
        curr_customer = row["cliente"]
        curr_order = row["pedido"]

        if curr_customer == customer and curr_order == "hamburguer":
            hamburgers += 1

    return hamburgers


def get_never_ordered_by_customer(data, customer):
    orders = set()
    orders_by_customer = set()

    for row in data:
        curr_customer = row["cliente"]
        curr_order = row["pedido"]

        orders.add(curr_order)

        if curr_customer == customer:
            orders_by_customer.add(curr_order)

    never_ordered = orders.difference(orders_by_customer)

    return never_ordered


def get_days_never_visited_by_customer(data, customer):
    days_open = set()
    visited_days = set()

    for row in data:
        curr_day = row["dia"]
        curr_customer = row["cliente"]

        days_open.add(curr_day)

        if curr_customer == customer:
            visited_days.add(curr_day)

    never_visited = days_open.difference(visited_days)

    return never_visited


def analyze_log(path):
    data = read_csv_file(path)

    most_ordered_by_maria = get_most_ordered_item_by_customer(data, "maria")
    total_burgers_by_arnaldo = get_total_burgers_ordered_by_customer(
        data, "arnaldo")
    never_ordered_by_joao = get_never_ordered_by_customer(data, "joao")
    never_visited_by_joao = get_days_never_visited_by_customer(data, "joao")

    content = (
        f"{most_ordered_by_maria}\n"
        f"{total_burgers_by_arnaldo}\n"
        f"{never_ordered_by_joao}\n"
        f"{never_visited_by_joao}\n"
    )

    write_to_file("data/mkt_campaign.txt", content)
