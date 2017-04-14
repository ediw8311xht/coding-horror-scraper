

def read_file(File):
    String = ""
    try:
        with open(File, 'r') as File:
            String = File.read()
    except:
        return 0
    return String

def write_file(String, File):
    try:
        f = open(File, 'w')
        f.write(String)
    except:
        pass
    f.close()

def write_line(String, pos, File):
    A = read_file(File)
    A = A.split("\n")
    if len(A) < pos + 1:
        A.append(String)
    else:
        A[pos] = String
    write_file("\n".join(A), File)
