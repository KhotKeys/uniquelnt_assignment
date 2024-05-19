def read_integers_from_file(file_name):
    try:
        with open(file_name, 'r') as file_object:
            integers = [int(line.strip()) for line in file_object.readlines()]
        return integers
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def remove_duplicates_and_sort(integers):
    return sorted(list(set(integers)))


def print_integers(integers):
    for integer in integers:
        print(integer)


def main_fuc():
    file_name = r'uniquelnt.txt'
    integers_list = read_integers_from_file(file_name)
    if integers_list:
        sorted_integers = remove_duplicates_and_sort(integers_list)
        print_integers(sorted_integers)


if __name__ == "__main__":
    main_fuc()
