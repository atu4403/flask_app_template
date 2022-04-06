from flask import Flask
from flask import render_template
from src.flask_app_template import settings, df

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", **settings)


@app.route("/hello")
def hello():
    settings["name"] = "jiro"
    settings["table1"] = df.to_html(classes="ui striped table", index=False)
    return render_template("hello.html", **settings)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
