import json

def load_data(file_path:str) -> dict | list:
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(file_path, data) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    pass

if __name__ == '__main__':
    main()