import json


# def remove_user(user_to_be_deleted: str, bank_path: str = "bank.json", auth_path: str = "auth.json",
# clients_path: str = "clients.json"):
#
#     with open(bank_path, "r") as f:
#         accounts = json.loads(f.read())
#
#     with open(auth_path, "r") as f:
#         credentials = json.loads(f.read())
#
#     with open(clients_path, "r") as f:
#         clients = json.loads(f.read())
#
#     accounts.pop(user_to_be_deleted, None)
#     credentials.pop(user_to_be_deleted, None)
#     clients.pop(user_to_be_deleted, None)
#
#     with open(bank_path, "w") as f:
#         f.write(json.dumps(accounts, indent=4))
#
#     with open(auth_path, "w") as f:
#         f.write(json.dumps(credentials, indent=4))
#
#     with open(clients_path, "w") as f:
#         f.write(json.dumps(clients, indent=4))


def remove_user(user_to_be_deleted: str, bank_path: str = "bank.json", auth_path: str = "auth.json",
                clients_path: str = "clients.json"):
    file_paths = [bank_path, auth_path, clients_path]

    for file_path in file_paths:
        with open(file_path, "r") as f:
            data = json.loads(f.read())

        data.pop(user_to_be_deleted, None)

        with open(file_path, "w") as f:
            f.write(json.dumps(data, indent=4))


def add_user(new_user: str, user_data: dict, bank_path: str = "bank.json", auth_path: str = "auth.json",
             clients_path: str = "clients.json"):
    file_paths = [bank_path, auth_path, clients_path]

    for file_path in file_paths:
        with open(file_path, "r") as f:
            data = json.loads(f.read())

        data[new_user] = user_data

        with open(file_path, "w") as f:
            f.write(json.dumps(data, indent=4))
