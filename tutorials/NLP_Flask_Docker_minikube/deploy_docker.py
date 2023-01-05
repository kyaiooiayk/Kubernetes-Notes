import model
import json

from flask import (
    Flask,
    request
)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/predict', methods=['POST'])
def predict():
    args = request.json
    X = model.featurize([args['text']], model.tfidf)
    labels = model.predict(X, model.clf).tolist()
    return json.dumps({'predictions': labels})


app.run(host=’0.0.0.0’)