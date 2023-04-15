from audio import combine_two_files
from models import SpeakerModel, Device, SampleRate
import easygui
import os
from text import get_separated_text_from_file
from push import push

tts = SpeakerModel()



# Can provide language, device, sample rate and model id
# Default       'ru'    'cpu'   48000           v3_1_ru
tts.specify_model()
info = tts.get_model_info()

def get_files() -> list:
    choice = easygui.buttonbox("Pick an item", "", ["File", "Folder"])
    if choice == "File":
        p = easygui.fileopenbox(filetypes=['*.txt'])
        files = [p]
    else:
        p = easygui.diropenbox(msg="Hello", title="Filessss")
        dir_listing = os.listdir(p)
        files = [f"{p}/{f}" for f in dir_listing if f.endswith(".txt")]
    return files

files = get_files()
output_audio_filename = easygui.enterbox("Specify outpyt file name") or ""

speaker = easygui.choicebox("Select voice", "", info.speakers)

for i, file in enumerate(files):
    print(file)
    try:
        paragraphs = get_separated_text_from_file(file)
    except Exception as e:
        print("Aborting program cause file can't be opened")
        exit()

    if len(files) == 1 and output_audio_filename:
        audio_filename = f"{output_audio_filename}.wav"
    else:
        audio_filename = f"{''.join(file.split('/')[-1].split('.')[:-1])}-{output_audio_filename}.wav"

    for j, p in enumerate(paragraphs):
        # push("Processing...", f"File {i+1}/{len(files)} paragraph {j+1}/{len(paragraphs)}")
        print("Processing...", f"File {i+1}/{len(files)} paragraph {j+1}/{len(paragraphs)}")
        try:
            tts.text2speech(p, "temp.wav", speaker=speaker)
        except Exception as e:
            print(e)
        combine_two_files([audio_filename, "temp.wav"], audio_filename)

easygui.msgbox("Process was finished", "Text-to-speech")


