from argparse import ArgumentParser
from typing import Callable
import os
import json

def main() -> None:
    parser = ArgumentParser(description="a simple cli tool to manage task")
    sub_parser = parser.add_subparsers(title="List of command", dest="command", required=True)

    add = sub_parser.add_parser("add", help="Add task to your list")
    add.add_argument("description", help="Description of your task")
    
    args = parser.parse_args().__dict__
    querie = get_querie(args.pop("command"))
    
    DATABASE_PATH : str = f"{os.getcwd()}\\database.json"
    
    database = load_database(DATABASE_PATH)
    
    if querie:
        querie(database, args["description"])
    else:
        print("Perintah tidak valid atau tidak ditemukan")
    
    # print(args["description"])

def load_database(path: str) -> dict[str, dict]:
    try:
        with open(path) as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {}
    
    return database

def get_querie(arg: str):
    if arg == 'add':
        return add_task
    return None

def add_task(database: dict[str, dict], description):
    print(database)
    print(f"Deskripsi Task adalah: {description}")

if __name__ == "__main__":
    main()