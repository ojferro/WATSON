
PATH_TO_MODEL= ~/deepspeech-venv/deepspeech-0.6.1-models/output_graph.pbmm
PATH_TO_AUDIO=~/deepspeech-venv/audio/2830-3980-0043.wav

python WATSON_client.py --model ~/deepspeech-venv/deepspeech-0.6.1-models/output_graph.pbmm --audio ~/deepspeech-venv/audio/2830-3980-0043.wav
