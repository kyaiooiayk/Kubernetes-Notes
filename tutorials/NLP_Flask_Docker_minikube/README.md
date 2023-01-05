# How to deploy a simple NLP model with Flask, Docker and minikube

***


## Step #0 - Get the data
- Download the Spam Text Message Classification dataset [here](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification?resource=download)

## Step #1 - Create a simple model
- This tutorial is intended to be a tutorial on deployment, thus the model details are not discussed. 
- Create a file called `model.py` containing:
```import csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


def load_data(fpath):
    print("Load data")
    # map ham -> 0, spam -> 1
    cat_map = {
        "ham": 0,
        "spam": 1
    }
    tfidf = TfidfVectorizer()
    msgs, y = [], []
    filein = open(fpath, "r")
    reader = csv.reader(filein)
    for i, line in enumerate(reader):
        if i == 0:
            # skip over the header
            continue
        cat, msg = line
        y.append(cat_map[cat])
        msg = msg.strip() # remove newlines
        msgs.append(msg)
    X = tfidf.fit_transform(msgs)
    return X, y, tfidf

def featurize(text, tfidf):
    print("Create feature")
    features = tfidf.transform(text)
    return features

def train(X, y, model):
    print("Train model")
    model.fit(X, y)
    return model

def predict(X, model):
    print("Predict")
    return model.predict(X)

clf = LogisticRegression()
X, y, tfidf = load_data('spamorham.csv')
train(X, y, clf)
```
***

## Step #2 - Create an end point with Flask
- Let’s set up Flask and create the endpoints for our model serving microservice. 
- Create a file called `deploy_local.py`:
```
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

app.run()
```
- The Flask app and ran it in `DEBUG` mode to start with so that it will alert us if any errors arise. Our app has a single `route` defined with the endpoint `/predict`. This is a POST endpoint that takes in a string of text and classifies it as either “ham” or “spam”. 
- We access the post arguments as `request.json`. There is a single argument, ‘text’ which specifies the text of the email message we’d like to classify. For efficiency purposes, we could also rewrite this to classify multiple pieces of text at once. You can try adding this feature if you want to :).
- The predict function is simple. It takes in an email message, converts it into a TF-IDF feature vector, then runs the trained logistic regression classifier to predict whether it is spam or ham. 
- Run the app with: `python deploy_local.py`
- This will spin a local Flask server runing at: http://127.0.0.1:5000/ or http://localhost:5000. 

## Step #3 - Test the API end point
- Create a file called `inference.py` having the following line:
```
import requests

res = requests.post('http://127.0.0.1:5000/predict', json={"text": "You are a winner U have been specially selected 2 receive ¬£1000 or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+)"})

# First method to get the result
print("Response | Prediction:", res.text)

# Second method to get the result
print("Response | Prediction:", res.json())
```
- This will make a POST request to the `/predict` endpoint with a json field that specifies the email message under the argument “text”. 
- This is clearly a spam message given a class label equal to 1.
***

## Step #4 - Create the Dockerfile
- We'd like to create Dockerfile for our text classification microservice. 
- To get this container to work, you’ll need to create a `requirements.txt` file which specifies the packages needed to run our microservice. You can create it by running this command in your terminal in that directory:  `pip freeze > requirements.txt`
- Change the code to our Flask script to get it working inside Docker. Just change the line that says `app.run()` to `app.run(host=’0.0.0.0’)`.
- Create a file called `Dockerfile` with the following content:
```
FROM python:3.9.7-slim
COPY requirements.txt /app/requirements.txt
RUN cd /app && pip install -r requirements.txt
ADD . /app
WORKDIR /app
ENTRYPOINT [“python”, “deploy_docker.py”]
```
- Where:
    - `FROM python:3.9.7-slim`, specifies the base image for our container. You can think of the image that our image inherits libraries, system configurations, and other elements from. The base image we use provides a minimal installation of Python v3.9.7.
    - `COPY requirements.txt /app/requirements.txt`  copies our `requirements.txt` file into the Docker image under the `/app` directory. `/app` will house our application files and related resources.
    - `RUN cd /app && pip install -r requirements.txt` we cd into /app and install our needed python libraries by running the command `pip install -r requirements.txt`. 
    - `ADD . /app` we add the contents of our current build directory into the /app folder with `ADD . /app`. This will copy over all of our Flask and model scripts.
    - `WORKDIR /app` we set the container’s working directory to /app by running `WORKDIR /app`. 
    - `ENTRYPOINT [“python”, “deploy_docker.py”]` 2e then specify the ENTRYPOINT, which is the command that the container will run when it is launched. We set it to run `python deploy.py`, which launches our Flask server.
***

## Step #5 - Build the Docker image
- To build your Docker image, run `docker build -t spam-or-ham-deploy .` from the directory that contains your Dockerfile. 
- To run your Docker container containing the Flask deployment script, type: `docker run -p 5000:5000 -t spam-or-ham-deploy`
- The `-p 5000:5000` flag publishes port 5000 in your container to port 5000 in your host. This makes your container’s service accessible from the ports on your machine. 
***

## Step #6 - Install minikube to run kubernetes locally
- The Flask API was designed to handle moderate request loads. If you’re deploying a large-scale service to millions of customers, you will need to make many adjustments to how you deploy the model.
- Kubernetes is a tool for orchestrating containers across large deployments. With Kubernetes, you can effortlessly deploy multiple containers across many machines and monitor all of these deployments. 
- To run Kubernetes locally, you will have to [install minikube](https://minikube.sigs.k8s.io/docs/start/).
***

## Step #7 - Launch minikube locally
- Next we’ll want to create a deployment by running: `kubectl create deployment hello-minikube --image=spam-or-ham-deploy`
- We then want to expose our deployment using: `kubectl expose deployment hello-minikube --type=NodePort --port=8080`
- Display some useful information about our service with: `kubectl get services hello-minikube`
- Launch the service in a browser with: `minikube service hello-minikube`
- View your service in the dashboard by running `minikube dashboard`
***

## References
- [How to Deploy NLP Models in Production ](https://neptune.ai/blog/deploy-nlp-models-in-production)
***