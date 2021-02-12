
PATH_TO_MODEL= ~/deepspeech-venv/deepspeech-0.6.1-models/output_graph.pbmm
PATH_TO_AUDIO=~/deepspeech-venv/audio/2830-3980-0043.wav

python3 WATSON_client.py --model ./models/deepspeech-0.9.3-models.pbmm --audio ./data/audio_rec_002.wav

