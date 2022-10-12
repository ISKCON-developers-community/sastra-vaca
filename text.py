from pathlib import Path

def text_input() -> str:
    return input("Insert here your text: ")

def input_text_file(file_path) -> str:

    p = Path("/home") / "sasha" / "Документы" / "Library" / "Официальные доки ИСККОН" / "Семинар Служите вайшнавам.txt"
    with open(file_path, "r") as f:
        text = f.read()
    return text

print(input_text_file(input("File path: ")))

def get_separated_text(filename: Path) -> list[str]:
    with open(filename, "r") as f:
        text = f.read()
    text_list = text.split('\n')
    new_list = []
    for t in text_list:
        if len(t.strip()) > 1:
            if len(t.strip()) > 1000:
                p = [s for s in t.split(". ") if len(s.strip()) > 1]
                new_list += p
            new_list.append(t)

    return new_list





