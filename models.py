from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import torch
from omegaconf import OmegaConf
from IPython.display import Audio

@dataclass
class ModelInfo():
    model_id: str
    languages: list[str]
    language: str
    device: str
    sample_rate: int
    speakers: list
    


class Device(Enum):
    CPU = 'cpu'
    GPU = 'cuda'

class SampleRate(Enum):
    HI = 48000
    MID = 24000
    LOW = 8000

class SpeakerModel:
    """
    Ititialize speaker's model object
    """
    def __init__(self):
        self.model_id = 'v3_1_ru'
        self.lang = 'ru'
        self.sample_rate = SampleRate.HI.value
        self.device = Device.CPU
        self.put_accent=True
        self.put_yo=True
        self.languages = []
        self.models = self.__get_models()

    def __get_models(self):
        """Get models from github"""
        try:
            if not Path('latest_silero_models.yml').exists():
                torch.hub.download_url_to_file(
                        'https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml',
                                    'latest_silero_models.yml',
                                    progress=False)
        except Exception:
            print("ERROR downloading models. You need internet connection")
            exit()

        self.models = OmegaConf.load('latest_silero_models.yml')
        self.languages = list(self.models.tts_models.keys())

    def specify_model(
            self,
            lang: str = None,
            device: Device = None,
            sample_rate: SampleRate = None,
            model_id: str = None):
        
        """
        Accept lenguage, device and
        """
        if lang: self.lang = lang
        if sample_rate: self.sample_rate = sample_rate.value
        if device: self.device = device
        if model_id: self.model_id = model_id
        set_device = torch.device(self.device.value)

        if self.lang not in self.languages:
            raise Exception(f"Language is not valid. You cat shoose from {self.languages}")
        
        
        self.model, self.example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                         model='silero_tts',
                                         language=self.lang,
                                         speaker=self.model_id)
        self.model.to(set_device)
        self.__get_speakers()


    def __get_speakers(self):
        """
        Gets the list of aviabble languages
        """
        try:
            audio = self.model.apply_tts(text='test',
                                    speaker="test",
                                    sample_rate=self.sample_rate,
                                    put_accent=self.put_accent,
                                    put_yo=self.put_yo)
        except Exception as err:
            self.speakers = str(err).split('`speaker` should be in ')[1].split(', ')
            self.speaker = self.speakers[0]

    def get_model_info(self):

            return ModelInfo(
                    model_id=self.model_id,
                    languages=self.languages,
                    language=self.lang,
                    device=self.device.value,
                    sample_rate=self.sample_rate,
                    speakers=self.speakers)

    def text2speech(self, text: str, filename: str, speaker: str = None) -> None: 
        audio = self.model.apply_tts(text=text,
                                speaker=speaker or self.speaker,
                                sample_rate=self.sample_rate,
                                put_accent=self.put_accent,
                                put_yo=self.put_yo)

        a = Audio(audio, rate=self.sample_rate)

        with open(filename, 'wb') as f:
            f.write(a.data)
