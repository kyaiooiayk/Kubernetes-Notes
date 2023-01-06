import requests

res = requests.post('http://127.0.0.1:5000/predict', json={"text": "You are a winner U have been specially selected 2 receive ¬£1000 or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+)"})

# First method to get the result
print("Response | Prediction:", res.text)

# Second method to get the result
print("Response | Prediction:", res.json())
