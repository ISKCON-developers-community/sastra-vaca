from os import listdir, getcwd
from os.path import isfile, join, basename

def get_txt_files():
  path = getcwd() + "/files"
  try:
    onlyfiles = [f"{path}/{f}" for f in listdir(path) if isfile(join(path, f)) and f.endswith('txt')]
  except:
    return []
  return onlyfiles