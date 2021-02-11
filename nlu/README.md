# To run simple action server + rasa core
```
rasa run actions
```

Open a new termial
```
rasa shell
```
Inputs to rasa shell will be sent to the actions server, and the corresponding custom action will be executed.

# To test NLU predictions
```
python3 endpoint_simple_test.py
```

# To add a new intent
Modify the contents of `master_file.json`, then run:
```
python3 add_intent.py
```
Add custom action implementation to `actions.py` file.





##### TO RUN VOICE TO TEXT + RASA:
# Run rasa server
rasa run --verbose --enable-api

# Run javascript application and go to localhost:8000
# This will start running the index.html and app.py files
uvicorn app:app --reload --port 8000


