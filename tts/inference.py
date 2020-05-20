# Must be running in pytorch conda env, as it is the one with all pkgs intalled

import torch
tacotron2 = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_tacotron2')
import numpy as np
from scipy.io.wavfile import write

tacotron2 = tacotron2.to('cuda')
tacotron2.eval()

waveglow = torch.hub.load('nvidia/DeepLearningExamples:torchhub', 'nvidia_waveglow')
# waveglow = torch.load('./waveglow_256channels_ljs_v2.pt')
waveglow = waveglow.remove_weightnorm(waveglow)
waveglow = waveglow.to('cuda')
waveglow.eval()

# text = 'there's a way to measure the acute emotional intelligence that has never gone out of style'

while True:
    text = input('Enter sentence to be spoken:')
    sequence = np.array(tacotron2.text_to_sequence(text, ['english_cleaners']))[None, :]
    sequence = torch.from_numpy(sequence).to(device='cuda', dtype=torch.int64)

    # run the models
    with torch.no_grad():
        _, mel, _, _ = tacotron2.infer(sequence)
        audio = waveglow.infer(mel)
    audio_numpy = audio[0].data.cpu().numpy()
    rate = 22050

    write('audio.wav', rate, audio_numpy)
