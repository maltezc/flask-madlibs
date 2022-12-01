from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def home():
    """ generates form for madlib """

    story_words = silly_story.prompts

    return render_template("questions.html", story_words=story_words)

@app.get("/results")
def show_results():
    """ displays generated madlib story """

    prompts = request.args

    text = silly_story.generate(prompts)

    return render_template("results.html", text=text)
