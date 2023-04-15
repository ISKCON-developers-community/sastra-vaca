from os import listdir, getcwd
from os.path import isfile, join, basename

def get_txt_files():
  path = getcwd() + "/files"
  print(path)
  try:
    onlyfiles = [f"{path}/{f}" for f in listdir(path) if isfile(join(path, f)) and f.endswith('txt')]
  except:
    return []
  return onlyfiles

def create_file() -> None:
  with open("files/hello.txt", "w") as my_file:
    my_file.write("Hello")

create_file()

print(get_txt_files())