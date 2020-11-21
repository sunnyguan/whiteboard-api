from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

stories_data = json.loads(open("stories.json").read())

@app.route('/stories')
@cross_origin()
def stories():
    return jsonify(stories_data)

