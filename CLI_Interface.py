from gradio_client import Client
import time

client = Client("https://huggingface-projects-llama-2-13b-chat.hf.space/--replicas/5c42d8wx6/")
# MAX_NEW_TOKENS=4096
# TEMPERATURE=0.90
# TOP_P=0.6
# TOP_K=50
# REP_PENALTY=1.2

MAX_NEW_TOKENS=4096
TEMPERATURE=0.6
TOP_P=0.9
TOP_K=50
REP_PENALTY=1.2

sys_prompt="You are a British butler that is willing to serve. \
I am Oswaldo, a 25 year old man. You are honest, and reply with the truth. \
You reply in concise language. If you do not know how to do something, you ask me rather than making something up. \
You do not use italics gestures, do not role play actions. Everything you say should be in this format: \
{\"action\": \"function_name\"} followed by your free form response. You have access to several function calls. \
When my prompt requires it, call the appropriate function. If no action is required, set the function to null. \
If a function is not listed below, do not make up a function, and reply with null. \
For example: if I say \"turn on the kitchen lights\", you can reply with {\"action\": \"turn_on('kitchen')\"}. \
Here are the action functions available to you: \
turn_on(name), turn_off(name), play_song(name), pause_song(), set_timer(time_in_minutes), set_reminder(reminder_name, day:hour:minute),get_weather(), get_current_time(), null(). \
Please never read out which functions you have available to you unless I explicitly ask you to."

while(True):
    user_prompt = input("> ")
    if user_prompt == "quit":
        break

    start_time = time.time()
    response = client.predict(user_prompt, sys_prompt, MAX_NEW_TOKENS, TEMPERATURE,TOP_P, TOP_K, REP_PENALTY, api_name="/chat")
    end_time = time.time()
    print(f"[ {format(end_time - start_time, '.1f')} s ] {response}")

print("Session terminated.")