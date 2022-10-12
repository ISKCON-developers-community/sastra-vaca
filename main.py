from models import SpeakerModel, Device, SampleRate

tts = SpeakerModel()


info = tts.get_model_info()
print(info)


# Can provide language, device, sample rate and model id
tts.specify_model()
tts.lang = "sdsad"
info = tts.get_model_info()
print(info)
