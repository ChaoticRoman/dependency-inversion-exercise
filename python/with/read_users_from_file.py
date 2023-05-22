from read_users import UserReader

class FileUserReader(UserReader):
    def read_users(self, fn="../users.txt"):
        with open(fn) as f:
            lines = [line.strip() for line in f.read().split("\n")]
        return [l for l in lines if l]

if __name__ == "__main__":
    print(FileUserReader().read_users())
