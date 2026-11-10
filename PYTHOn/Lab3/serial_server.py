import flask
import plateloader
import threading


<<<<<<< HEAD

app = flask.Flask(__name__, static_url_path='', static_folder='Public')

serial_lock = threading.Lock()
loader = plateloader.PlateLoader()


@app.route("/")
=======
app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
loader = plateloader.PlateLoader() # TODO: Set the port if needed.

@app.get("/")
>>>>>>> efaa187044a506041cdf3ccd22cfb4d9fa4dd0f6
def handle_naked_domain():
    return flask.redirect("/index.html")

@app.get("/api/<command>")
def handle_plateloader_commands(command):
    with serial_lock:
        response = loader.send_command(command)
<<<<<<< HEAD
    return "Success!"


if __name__ == "__main__":
    print("Running Flask!")
    loader.connect()
    app.run(host = '0.0.0.0', port = 8080, debug = True)
=======
    return response


if __name__ == "__main__":
    print("Running flask!")
    loader.connect()
    try:
        app.run(host="0.0.0.0", port=8080, use_reloader=False)
    finally:
        print("Disconnecting plate loader")
        loader.disconnect()
>>>>>>> efaa187044a506041cdf3ccd22cfb4d9fa4dd0f6
