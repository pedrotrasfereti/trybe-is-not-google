from .analyze_log import (
    get_most_ordered_item_by_customer,
    # get_never_ordered_by_customer,
    # get_days_never_visited_by_customer
)


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append({"cliente": customer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_customer(self, customer):
        return get_most_ordered_item_by_customer(self._data, customer)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
