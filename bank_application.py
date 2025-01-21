import os
import json
import time
from getpass import getpass
from colorama import init, Fore, Style

import pwinput
import admin_operations

# Initializează colorama
init(autoreset=True)

USER_MENU = f"""
{Fore.GREEN}1.Sa ceara bank statement -> valoare contului{Style.RESET_ALL} 
{Fore.GREEN}2. Sa transfere unui alt utilizator{Style.RESET_ALL}
{Fore.GREEN}3. Sa scoata bani din cont{Style.RESET_ALL}
{Fore.GREEN}4. Sa adauge bani in cont{Style.RESET_ALL}
{Fore.GREEN}5. Sa converteasca banii{Style.RESET_ALL}
{Fore.RED}6. Sign out{Style.RESET_ALL}
{Fore.YELLOW}7. Exit{Style.RESET_ALL}

Type in choice: """

ADMIN_MENU = f"""
{Fore.BLUE}1. Sa se stearga clientul (admin-only){Style.RESET_ALL}
{Fore.BLUE}2. Sa adauge un client nou (admin-only){Style.RESET_ALL}
{Fore.RED}3. Sign out{Style.RESET_ALL}
{Fore.GREEN}4. Show users{Style.RESET_ALL}
{Fore.YELLOW}5. Exit{Style.RESET_ALL}
"""

# ENVIRONMENT VARIABLE
# print(os.environ['admin_bank'])


def login(user: str, auth_path: str = "auth.json") -> str:
    if user == "admin":
        for _ in range(3):
            passwd = getpass(f"{Fore.GREEN}Type in password: {Style.RESET_ALL}")
            if passwd == os.environ['admin_bank']:
                return user
        return ""
    else:
        with open(auth_path, "r") as f:
            credentials = json.loads(f.read())

        while user not in credentials:
            print(f"{Fore.BLUE}User found in database.{Style.RESET_ALL}")
            user = input(f"{Fore.YELLOW}Type in ID user: {Style.RESET_ALL}")

        passwd = input(f'{Fore.MAGENTA}PW: {Style.RESET_ALL}')

        while passwd != credentials[user]:
            passwd = input(f"{Fore.RED}Wrong password: {Style.RESET_ALL}")

        return user

def account_balance(user: str, bank_path: str = "bank.json") -> str:
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    value = accounts[user]["value"]
    currency = accounts[user]["currency"]

    return f"{Fore.MAGENTA}Your account is worth : {value}{currency}"


def convert_account(user: str, to_currency: str, bank_path: str = "bank.json"):
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    account = accounts[user]
    account["value"] = convert_currency(account['value'], account["currency"], to_currency)
    account["currency"] = to_currency

    with open(bank_path, "w") as f:
        f.write(json.dumps(accounts, indent=4))

        # return "Account converted from x to y"


def convert_currency(amount: int, from_currency: str, to_currency: str, currencies_json = "currencies.json") -> int:
    with open(currencies_json, "r") as f:
        conversion_rates = json.loads(f.read())

    amount = amount * conversion_rates[from_currency][to_currency]

    return amount

def transfer_money(sender: str, receiver: str, amount: int, bank_path: str = "bank.json"):
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    if amount <= accounts[sender]["values"]:
        if accounts[sender]["currency"] == accounts[receiver]["currency"]:
            accounts[receiver]["value"] += amount
            accounts[sender]["value"] -= amount
        else:
            amount_receiver_currency = convert_currency(amount, accounts[sender]["currency"], accounts[receiver]["currency"])
            accounts[receiver]["value"] += amount_receiver_currency
            accounts[sender]["value"] -= amount

        with open(bank_path, "w") as f:
            f.write(json.dumps(accounts, indent=4))

        print(f"{Fore.GREEN}Ati transferat cu succes. Cont curent: {Style.RESET_ALL}{accounts[sender]['value']} {accounts[sender]['currency']}")

    else:
        print(f"{Fore.RED}Not enough money to send.{Style.RESET_ALL}")


def withdraw_money(user: str, amount: int, bank_path: str = "bank.json"):
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    if user in accounts["value"]:
        if amount <= accounts:
            return user


def get_username_by_phone(phone_number: str, clients_path: str = "clients.json"):
    with open(clients_path, "r") as f:
        clients = json.loads(f.read())

    for user_id, details in clients.items():
        if details["phone"] == phone_number:
            return user_id

    print(f"{Fore.RED}Phone number not found.{Style.RESET_ALL}")
    return None

if __name__ == '__main__':
    username = input(f"{Fore.BLUE}Please enter your username: {Style.RESET_ALL}")
    username = login(username)
    menu = USER_MENU if username != "admin" else ADMIN_MENU

    user_pick = input(menu)

    while True:
        if username != "admin":
            match user_pick:
                case "1":
                    print(account_balance(username))
                case "2":
                    amount = int(input(F"{Fore.BLUE}Amount of money in your current currency: {Style.RESET_ALL}"))
                    phone_number = input(f"{Fore.BLUE}Who is the receiver? {Style.RESET_ALL}")
                    receiver_id = get_username_by_phone(phone_number)
                    if receiver_id:
                        transfer_money(username, receiver_id, amount)
                case "3":
                    amount = int(input(f"{Fore.BLUE}How much would you like to withdraw? {Style.RESET_ALL}"))
                    try:
                        withdraw_money(username, amount)
                        print(f"{Fore.GREEN}Withdrawal successful!{Style.RESET_ALL}")
                    except Exception as e: print(
                        f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

                case "4":
                    pass
                case "5":
                    currency = input(f"{Fore.BLUE}What currency do you need to transfer? {Style.RESET_ALL}")
                    # verificati sa fie currency corect
                    convert_account(username, currency)
                case "6":
                    username = input(f"{Fore.GREEN}Type a new user: {Style.RESET_ALL}")
                    username = login(username)
                case "7":
                    exit(0)
                case "8":
                    pass
                case _:
                    pass
            time.sleep(3)
            menu = USER_MENU if username != "admin" else ADMIN_MENU
            user_pick = input(menu)
        else:
            match user_pick:
                case "1":
                    user_to_delete = input(f"{Fore.YELLOW}Which user do you want to delete? {Style.RESET_ALL}")
                    admin_operations.remove_user(user_to_delete)
                case "2":
                    pass
                case "3":
                    username = input(f"{Fore.BLUE}Input a new user: {Style.RESET_ALL}")
                    username = login(username)
                case "4":
                    with open("bank.json", "r") as f:
                        print(f.read())
                case "5":
                    exit(0)
                case _:
                    pass

        time.sleep(3)
        menu = USER_MENU if username != "admin" else ADMIN_MENU
        user_pick = input(menu)


