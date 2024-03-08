from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hi World"

if __name__ == "__main__":
    app.run()