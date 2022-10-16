from audio import combine_two_files
from models import SpeakerModel, Device, SampleRate
import easygui
from text import get_separated_text_from_file, Files, PathType
from push import push

tts = SpeakerModel()



# Can provide language, device, sample rate and model id
# Default       'ru'    'cpu'   48000           v3_1_ru
tts.specify_model()
info = tts.get_model_info()
choice = easygui.buttonbox("Pick an item", "", ["File", "Folder"])
if choice == "File":
    p = easygui.fileopenbox(filetypes=['*.txt'])
else:
    p = easygui.diropenbox(msg="Hello", title="Filessss")
paragraphs = get_separated_text_from_file(
        Files(
            path=p,
            type= PathType.FILE if choice == 'File' else PathType.DIR))
speaker = easygui.choicebox("Select voice", "", info.speakers)

audio_filename = easygui.enterbox("Specify outpyt file name") + ".wav"
for i, p in enumerate(paragraphs):
    push("Processing...", f"Paragraph {i+1} from {len(paragraphs)}")
    try:
        tts.text2speech(p, "temp.wav", speaker=speaker)
    except Exception:
        print(p)
    combine_two_files([audio_filename, "temp.wav"], audio_filename)

easygui.msgbox("Process was finished", "Test-to-speech")


