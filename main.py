from flask import Flask, render_template
from blueprints.user_platform.__init__ import user_platform

app = Flask(__name__)


app.register_blueprint(user_platform, url_prefix="/platform")


@app.route("/")
def main():
    return render_template("home_page.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
