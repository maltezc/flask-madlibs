from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# home page with form
@app.get("/")
def home():
    story_words = silly_story.prompts

    return render_template("questions.html", story_words=story_words)


# results
@app.get("/results")
def show_results():

    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]



