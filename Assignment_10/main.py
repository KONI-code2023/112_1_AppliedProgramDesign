# ======================
# file: main.py
# author: KNE-code2023@github
# date: 2024-01-08
# ======================
import os
import json
import subprocess


CODE_FOLDER = ".\\code"
DESC_FILE = ".\\config\\config.json"


def get_programs() -> dict:
    programs = {}
    for file_name in os.listdir(CODE_FOLDER):
        if file_name.endswith(".py"):
            name = os.path.splitext(file_name)[0].upper()
            programs[name] = {"file": os.path.join(CODE_FOLDER, file_name), "desc": "No desc"}
    return programs


def load_descriptions() -> dict:
    descriptions = {}
    try:
        with open(DESC_FILE, "r", encoding="utf-8") as file:
            descriptions = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return descriptions


def update_descriptions(programs: dict, descriptions: dict) -> None:
    for program_name, info in programs.items():
        if program_name in descriptions:
            info["desc"] = descriptions[program_name]


def run(file: str) -> None:
    try:
        subprocess.run(["python", file], check=True)
        print("Done.")
    except subprocess.CalledProcessError as error:
        print(f"[Error] Unable to execute file '{file}': {error}")


def display_menu(programs: dict, descriptions: dict) -> None:
    sorted_programs = dict(sorted(programs.items()))
    #max_title_length = max(len(descriptions[option]["title"]) for option in sorted_programs)
    print("\n====================================\
           \nMain Menu\
           \n====================================")
    for option, info in sorted_programs.items():
        title = descriptions.get(option, {}).get("title", "No title")
        author = descriptions.get(option, {}).get("author", "No author")

        #print(f"{option}) {title}{'  '*(max_title_length - len(title))} [developed by {author}]")
        print(f"{option}) {title}")

    print("\nZ) Exit Menu")
    print("====================================")


def main() -> None:
    programs = get_programs()
    descriptions = load_descriptions()
    update_descriptions(programs, descriptions)

    while True:
        display_menu(programs, descriptions)
        user_input = input("Please enter the letter of the option you desire (A ~ E or Z):\n ").upper()

        if user_input == "Z":
            print("Exit Menu ...")
            break
        elif user_input in programs:
            print(f"Run {user_input}.py ...")
            run(programs[user_input]["file"])
        else:
            print(f"[Error] Unable to open file '{user_input}.py': File or directory not found")


if __name__ == "__main__":
    main()
