from TTS.api import TTS
import numpy as np

tts = TTS('tts_models/en/vctk/vits')

count = 0
while(True):
    count += 1
    input_text = input("Enter input text: ")
    if input_text == 'Q':
        break

    wav_out = tts.tts_to_file(text=input_text, speaker='p335', file_path=f"./output_samples/{count}_out.wav")
