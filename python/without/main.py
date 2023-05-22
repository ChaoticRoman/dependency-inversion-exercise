import read_users

if __name__ == "__main__":
    username = input("username: ").strip()
    if username in read_users.read_users():
        print("Logged in.")
    else:
        print("Denied.")
