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


@app.route('/')
def uiStory():
    return """<html>
    <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">
    </head>
    <body>
        <h1>Add a story!</h1>
        <form method="GET" action = "/addStory">
        <div class="form-group">
            <label for="text">Text</label>
            <input id="text" type="radio" name="type" value="text" />
            <br>
            <label for="photo">Photo</label>
            <input id="photo" type="radio" name="type" value="photo" />
            <br>
            <input type="text" name="data" placeholder="link or text content" />
        </div>
        <input class="btn btn-primary" type="submit" value="submit">
        </form>

    </body>
    </html>"""