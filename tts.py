from pathlib import Path
from models import SpeakerModel
from audio import combine_audio_files
from time import sleep

from text import get_separated_text

p = Path("/home") / "sasha" / "Документы" / "Library" / "Официальные доки ИСККОН" / "Семинар Служите вайшнавам.txt"
tts = SpeakerModel()


info = tts.get_model_info()

#lang = input(f'Choose you language from {info.languages}\nYour choise: ')

tts.specify_model()

tt1 = """
Первая глава озаглавлена «Бх+аума» — земная. В ней описывалось как совершается преданное служение на Земле. Однако мы отметили, что Земля — это конечное место для служения. Чтобы вернуться во Вриндаван, необходимо вернуться на Землю. Даже для того, чтобы выбраться из материальной природы, необходимо вернуться на Землю.
"""

tt2 = """
Во второй части мы отметим, что после того, как Гоп Кумар побывал на Сатьялоке и достиг положения Брахмы, он вернулся на Землю во Вриндаван. После того, как он исполнял преданное служение во Вринд+аване, он получил дополнительные наставления от духовного уч+ителя и достиг квалификации, чтобы выбраться из материального мира.
"""

text_list = get_separated_text(p)

files = []
for i, t in enumerate(text_list[:4]):
    filename = f"a-file{i}"
    print(filename, t)
    if not t:
        continue
    files.append(filename)
    result = tts.text2speech(t, filename, speaker='baya')


if len(files) > 1:
    combine_audio_files(files)
