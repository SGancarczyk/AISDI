#   Reading from txt


def read_from_txt(file_name):
    #   Returns a list with words from file

    with open(file_name, 'r') as file:
        data = []
        for line in file:
            data.extend(line.strip().split())
    return data
