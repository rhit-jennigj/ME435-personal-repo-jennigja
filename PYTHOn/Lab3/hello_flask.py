import flask

app = flask.Flask(__name__)


@app.route("/")
def hello_route():
    return "<h1 style='font-size: 400px;'>joey gay</h1>"


if __name__ == "__main__":
    print("Running Flask!")
    app.run(host = '0.0.0.0', port = 8080, debug = True)
