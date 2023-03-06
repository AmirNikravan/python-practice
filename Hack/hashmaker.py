def make_hash():
    with open("/tmp/sha256.txt", "w") as file:
        for i in range(0, 10000):
            file.write(f"{i} = {str(hash(str(i).zfill(4)))}\n")


def hashtodict():
    with open("/tmp/sha256.txt") as file:
        passes = dict()
        for i in range(0, 19):
            passes[file.readline()[4:].strip()] = i
        print( passes)