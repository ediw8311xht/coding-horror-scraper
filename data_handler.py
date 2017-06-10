import readwrite

test_file = "saved data.txt"

def get_data(txtfile):
    list_file = readwrite.read_file(txtfile).split()
    data = [None, None]
    for i in range(0, len(list_file)):
        if "~" in list_file[i][0]:
            data[0] = list_file[i][1:]
        elif ".txt" in list_file[i]:
            data[1] = list_file[i]
    return data

if __name__ == "__main__":
    print(get_data(test_file))
