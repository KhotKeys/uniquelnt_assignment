
def integers_file(file):
    try:
        with open(file, 'r') as file:
            integers = file.readlines()
            integers = [int(line.strip()) for line in integers]
        return integers
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []


def get_unique_sorted_integers(integers):
    unique_integers = list(set(integers))

    unique_integers.sort()

    return unique_integers


def main():
    file = r'uniquelnt.txt'
    integers = integers_file(file)

    if integers:
        unique_sorted_integers = get_unique_sorted_integers(integers)
        for integer in unique_sorted_integers:
            print(integer)


if __name__ == "__main__":
    main()