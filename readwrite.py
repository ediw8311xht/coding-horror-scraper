
def read_file(File):
    string_var = ""
    try:
        with open(File, 'r') as fi:
            string_var = fi.read()
    except:
        print("no file")
        return "no file"
    return string_var

def write_file(string_var, File):
    try:
        fi = open(File, 'w')
        fi.write(string_var)
    except:
        print("no file")
        return False
    fi.close()
    return True

def write_line(string_var, pos, File):
    A = read_file(File)
    if A == "no file":
        A = ""
    A = A.split("\n")
    if len(A) < pos + 1:
        A.append(string_var)
    else:
        A[pos] = string_var
    return write_file("\n".join(A), File)

def add_line(string_var, File):
    try:
        with open(File, "a") as fi:
            fi.write(string_var)
    except:
        print("no file")
        return False
    return True

def create_file(file_name):
    if read_file(file_name) != "no file":
        return False
    write_file("", file_name)
    return True
