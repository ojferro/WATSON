import subprocess as sp
import json

print("\nThis is a simple script to test that the nlu model is working as expected.")
print("In a separate terminal, run: rasa run --enable-api -m models/nlu-20200605-223158.tar.gz\n\n")

template = 'curl localhost:5005/model/parse -d \'{{\"text\":\"{}\"}}\''
bot_message = ""
while bot_message != "Bye":
	message = input("\n>: ")

	proc = sp.Popen(template.format(message), shell=True, stdout=sp.PIPE, stderr=sp.DEVNULL)
	resp, err = proc.communicate()
	
	# Verify that the nlu server is running
	if not resp:
		print("Connection refused. Ensure server is running:")
		print("rasa run --enable-api -m models/<model-name.tar.gz>")
		break
	resp_json = json.loads(resp)

	print(json.dumps(resp_json, indent=2))