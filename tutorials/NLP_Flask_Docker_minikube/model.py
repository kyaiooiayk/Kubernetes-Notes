import csv
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