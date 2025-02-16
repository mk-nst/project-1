import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File {path} does not exist")
    with open(path, "r") as file:
        return file.read()

def write_file(path: str, content: str):
    with open(path, "w") as file:
        file.write(content)