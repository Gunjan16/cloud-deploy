from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Jenkins Pipeline!"
# run the app.
if __name__ == "__main__":
    app.run()
