# functia nr 1 sa se construieasca o functie care sa primeasca path-ul unui fisier si tipul de operatie, text pe care sa il scrie daca este de scris ceva.
# functia nr 2 este sa ia un fisier sa incerce linie cu linie sa construieasca un dictionar
import json


def execute_on_file(path: str, operator: str = "r", text_to_write: str = ""):
    try:
        with open(path, operator) as f:
            if operator == "r":
                return f.read()
            elif operator == "w" or operator == "a":
                f.write(text_to_write)
    except FileNotFoundError as e:
        print("File not found at specific path...creating new file")
        open(path, 'a').close()
    except Exception as e:
        print(f"Exceptia este neprevazuta {e}")


def parse_txt_to_dict(text_data: str) -> dict:
    try:
        lines = text_data.split("\n")
        my_dict = {}
        for line in lines:
            try:
                key, value = line.split(":")
                my_dict[key] = value
            except Exception as e:
                print("Linia nu este potrivita")
            return my_dict
    except Exception as e:
        print("Fisierul este gol. Scrie ceva in el.")


if __name__ == '__main__':
    while True:
        text = execute_on_file("cba.txt")
        my_dict = parse_txt_to_dict(text)
        execute_on_file('"cba.txt", "w", json.dumps(my_dict, indent=4')
