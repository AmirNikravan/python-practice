from hashlib import sha256
def make_hash():
    with open("./sha256.txt", "w", encoding="utf-8") as file:
        for i in range(0, 10000):
            file.write(f"{str(i).zfill(4)} = {sha256((str(i).zfill(4).encode())).hexdigest()}\n")
        


def hashtodict():
    with open("./sha256.txt") as file:
        passes = dict()
        for i in range(0, 10000):
            passes[file.readline()[6:].strip()] = str(i).zfill(4)
        return(passes)
