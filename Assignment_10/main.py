# ======================
# file: main.py
# author: KNE-code2023@github
# date: 2024-01-08
# ======================
import os
import json
import subprocess
import platform 

# 存放程式碼的資料夾
CODE_FOLDER = "./code"
# 描述檔
DESC_FILE = "./desc.json"


def get_progs() -> dict:
    progs = {}
    for fname in os.listdir(CODE_FOLDER):
        if fname.endswith(".py"):
            # 取得檔案名稱（拿掉副檔名並轉成大寫）
            name = fname.split(".")[0].upper()
            progs[name] = {"file": os.path.join(CODE_FOLDER, fname),
                           "desc": "No desc"}
    return progs


def load_desc() -> dict:
    descs = {}
    try:
        with open(DESC_FILE, "r", encoding="utf-8") as f:
            # 將 JSON 解析成字典
            descs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return descs


def update_desc(progs: dict, descs: dict) -> None:
    for pname, info in progs.items():
        if pname in descs:
            info["desc"] = descs[pname]


def run(file: str) -> None:
    try:
        # 使用 subprocess 執行 Python 程式
        if platform.system() == "Windows":
            subprocess.run(["python", file], check=True, shell=True)
        else:
            subprocess.run(["python", file], check=True)
        print("done")
    except subprocess.CalledProcessError:
        print(f"[Error] unable to run file '{file}'")


def menu() -> None:
    # 將程式清單字典照字母順序排序
    sorted_progs = dict(sorted(PROGRAMS.items()))

    print("\n=========== Main Menu ===========")
    for opt, info in sorted_progs.items():
        print(f"{opt}) {info['desc']}")

    print("\nZ) Exit")
    print("=================================")


def main() -> None:
    global PROGRAMS
    PROGRAMS = get_progs()
    descs = load_desc()
    update_desc(PROGRAMS, descs)

    while True:
        menu()
        user_in = input("Select from the menu:\n ").upper()

        if user_in == "Z":
            print("Exit ")
            break
        elif user_in in PROGRAMS:
            print(f"Run {user_in}.py ...")
            run(PROGRAMS[user_in]["file"])
        else:
            print(f"[Error] can't open file '{user_in}.py': No such file or directory")


if __name__ == "__main__":
    main()
