import flask
import threading
import LEDONOFF

app = flask.Flask(__name__, static_url_path="", static_folder="public")

serial_lock = threading.Lock()
LED = LEDONOFF.LEDONOFF() 
LED.connect()         

@app.route("/")
def hello_naked_domain():
    return flask.redirect("/exam1.html")
    
@app.get("/api/led/<command>")
def handle_LED_commands(command):
    with serial_lock:
        response = LED.ONOFF("LED " + command)
    return response

@app.get("/api/flash/<count>/<delaytime>")
def handle_Flash_commands(count, delaytime):
    with serial_lock:
        response = LED.flash(count, delaytime)
    return response

if __name__ == "__main__":
    print("Running Flask!")
    app.run(host='0.0.0.0', port=8080, use_reloader=False) # use_reloader=False
    print("Hi")