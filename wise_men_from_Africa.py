def integers_file(file_name):
    try:
        with open(file_name, 'r') as file_object:
            unique_integers_flow = file_object.readlines()
            nique_integers_flow  = [int(line.strip()) for line in unique_integers_flow]
        return nique_integers_flow
    except Exception as e:
        print(f"When there is an error in the file: {e}")
        return []


def get_unique_sorted_integers(integers):
    unique_integers = list(set(integers))
   
    unique_integers.sort()
   
    return unique_integers

def main():
    file_name = r'uniquelnt.txt' 
    integers = integers_file(file_name)
    
    if integers:
        unique_sorted_integers = get_unique_sorted_integers(integers)
        for integer in unique_sorted_integers:
            print(integer)
            
if __name__ == "__main__":
    main()
