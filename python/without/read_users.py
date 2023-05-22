def read_users(fn="../users.txt"):
    with open(fn) as f:
        lines = [line.strip() for line in f.read().split("\n")]
    return [l for l in lines if l]

if __name__ == "__main__":
    print(read_users())
