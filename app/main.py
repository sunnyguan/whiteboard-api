from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
import json
import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

stories_data = json.loads(open("stories.json").read())

@app.route('/stories')
@cross_origin()
def stories():
    return jsonify(stories_data)

@app.route('/addStory')
@cross_origin()
def addStory():
    story_type = request.args.get('type')
    story_len = request.args.get('duration', default = 3, type = int)
    story_text = request.args.get('data')
    newStory = {
        "type": story_type,
        "length": story_len,
        "src": story_text,
        "time": int(time.time())
    }
    stories_data[0]["items"].append(newStory)
    with open('stories.json', 'w') as f:
        json.dump(stories_data, f)
        print("Stories updated!")
    return jsonify(stories_data)