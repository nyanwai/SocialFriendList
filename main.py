import json
import random
import os

def generate_random_id():
    return random.randint(1000, 9999)

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    return {"users": []}

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def add_user(data):
    username = input("Enter username: ")
    user = {
        "username": username,
        "id": generate_random_id(),
        "social_score": 500
    }
    data["users"].append(user)
    print(f"User {username} added with ID {user['id']} and default social score {user['social_score']}.")

def display_users(data):
    print("------------------------------")
    for user in data["users"]:
        print(f"username: {user['username']}")
        print(f"id: {user['id']}")
        print(f"social score: {user['social_score']}")
        print("------------------------------")
    print()

def edit_score(data):
    print("Current Usernames:")
    for user in data["users"]:
        print(user["username"])
    username = input("Enter username to edit score: ")
    for user in data["users"]:
        if user["username"] == username:
            print(f"Current social score for {username}: {user['social_score']}")
            delta = int(input("Enter delta value (+/-): "))
            user["social_score"] += delta
            print(f"Social score for user {username} updated by {delta}. New score: {user['social_score']}.")
            return
    print(f"User '{username}' not found.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    filename = 'db.json'
    data = load_data(filename)

    while True:
        command = input("Enter command (add/display/edit/exit): ").strip().lower()
        if command == "add":
            clear_terminal()
            add_user(data)
            save_data(filename, data)
        elif command == "display":
            clear_terminal()
            display_users(data)
        elif command == "edit":
            clear_terminal()
            edit_score(data)
            save_data(filename, data)
        elif command == "exit":
            print("Exiting the program.")
            break
        else:
            clear_terminal()
            print("Unknown command. Please use 'add', 'display', 'edit', or 'exit'.")

if __name__ == "__main__":
    main()
