import flask
import json
from flask import request
import tensorflow_hub as hub


app = flask.Flask('encoder')

@app.route('/', methods=['post'])
def home():
    payload = request.json  # payload should be like ["asdfasdf","asdfasdf"]
    print(payload)
    embeddings = embed(payload)
    result = [{'vector':str(i.numpy().tolist()),'string':j} for i,j in zip(embeddings, payload)]
    return flask.Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    app.run(host='0.0.0.0', port=999)