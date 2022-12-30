def get_separated_text_from_file(file: str, repl_dict=None) -> list[str]:
    new_list = []
    with open(file, "r") as f:
        text = f.read()
    text_list = text.split('\n')
    for t in text_list:
        if len(t.strip()) > 1:
            if len(t.strip()) > 1000:
                p = [s for s in t.split(". ") if len(s.strip()) > 1]
                new_list += p
            else:
                new_list.append(t)

    return replace_by_dict(new_list, repl_dict) if repl_dict else new_list


def replace_by_dict(paragraphs: list[str], repl_dict: dict) -> list[str]:
    return paragraphs


