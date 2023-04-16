from audio import combine_two_files
from files import get_txt_files
from models import SpeakerModel, Device, SampleRate
from text import get_separated_text_from_file

tts = SpeakerModel()



# Can provide language, device, sample rate and model id
# Default       'ru'    'cpu'   48000           v3_1_ru
tts.specify_model()
info = tts.get_model_info()


files = get_txt_files()
output_audio_filename = input("Type output file name: ") or "audio"

speaker = input(f"Select voice. Type one of: {'/'.join(info.speakers)} :") or info.speakers[0]
print(f"Selected voice - {speaker}")

for i, file in enumerate(files):
    try:
        paragraphs = get_separated_text_from_file(file)
    except Exception as e:
        print("Aborting program cause file can't be opened")
        exit()

    if len(files) == 1 and output_audio_filename:
        audio_filename = f"files/{output_audio_filename}-{speaker}.wav"
    else:
        audio_filename = f"files/{''.join(file.split('/')[-1].split('.')[:-1])}-{speaker}-{output_audio_filename}.wav"

    for j, p in enumerate(paragraphs):
        # push("Processing...", f"File {i+1}/{len(files)} paragraph {j+1}/{len(paragraphs)}")
        print("Processing...", f"File {i+1}/{len(files)} paragraph {j+1}/{len(paragraphs)}")
        try:
            tts.text2speech(p, "files/temp.wav", speaker=speaker)
        except Exception as e:
            print(e)
        combine_two_files([audio_filename, "files/temp.wav"], audio_filename)

print("Process was finished")


