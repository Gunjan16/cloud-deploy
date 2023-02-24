from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "My new App!"
# run the app.
if __name__ == "__main__":
    app.run()
