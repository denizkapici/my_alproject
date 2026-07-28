def remove_duplicates(input_list):
    seen = set()
    output_list = [x for x in input_list if not (x in seen or seen.add(x))]
    return output_list

if __name__ == '__main__':
    input_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    output_list = remove_duplicates(input_list)
    print("Output list without duplicates: ", output_list)