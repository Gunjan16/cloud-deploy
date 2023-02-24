from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Good!"
# run the app.
if __name__ == "__main__":
    app.run()
