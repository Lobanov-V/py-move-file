import os


def move_file(command: str) -> None:
    _, src, dest = command.split()

    if dest.endswith("/"):
        dest = dest + src.split("/")[-1]

    parts = dest.split("/")
    path = ""

    for folder in parts[:-1]:
        path = folder if not path else path + "/" + folder
        if not os.path.exists(path):
            os.mkdir(path)

    with open(src, "r") as file:
        content = file.read()

    with open(dest, "w") as file:
        file.write(content)

    os.remove(src)
