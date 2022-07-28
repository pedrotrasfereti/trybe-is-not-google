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


def analyze_log(path_to_file):
    raise NotImplementedError
