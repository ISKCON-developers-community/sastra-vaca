from dataclasses import dataclass
from enum import Enum
import os

class PathType(Enum):
    FILE = 'file'
    DIR = 'folder'

@dataclass
class Files:
    type: PathType
    path: str
    

def get_separated_text_from_file(file: Files, repl_dict=None) -> list[str]:
    new_list = []
    if file.type == PathType.FILE:
        files = [file.path]
    else:
        dir_listing = os.listdir(file.path)
        files = [f"{file.path}/{f}" for f in dir_listing if f.endswith(".txt")]
    for filepath in files:
        with open(filepath, "r") as f:
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


