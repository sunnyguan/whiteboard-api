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
    story_cat = request.args.get('cat', default = 0, type = int)
    newStory = {
        "type": story_type,
        "length": story_len,
        "src": story_text,
        "time": int(time.time())
    }
    stories_data[story_cat]["items"].append(newStory)
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
    <body style="display: flex; width: 100%; justify-content: center">
        <div style="margin: auto">
            <h1>Add a story!</h1>
            <form method="GET" action = "/addStory">
            <div class="form-group">
                <input id="text" type="radio" name="type" value="text" />
                <label for="text">Text</label>
                <input id="photo" type="radio" name="type" value="photo" />
                <label for="photo">Photo</label>
            </div>
            <div class="form-group">
                <label for="data">Link/Text: </label>
                <input type="text" id="data" name="data" placeholder="link or text content" /><br>
            </div>
            <div class="form-group">
                <label for="duration">Duration: </label>
                <input type="text" id="duration" name="duration" value="3" />
            </div>
            <div class="form-group">
                <label for="cat">Choose a category:</label>
                <select name="cat" id="cat">
                    <option value="0">Temoc</option>
                    <option value="1">Stolen Memes</option>
                    <option value="2">Tobor</option>
                    <option value="3">Dr. Page</option>
                    <option value="4">Prof. Haas</option>
                    <option value="5">Enarc</option>
                </select>
            </div>
            <input class="btn btn-primary" type="submit" value="submit">
            </form>
        </div>
    </body>
    </html>"""