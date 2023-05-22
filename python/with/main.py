from read_users_from_file import FileUserReader

if __name__ == "__main__":
    username = input("username: ").strip()

    reader = FileUserReader()
    if username in reader.read_users():
        print("Logged in.")
    else:
        print("Denied.")
