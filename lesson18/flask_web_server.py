from flask import Flask

app = Flask("sample_web_app")

@app.route("/")
def hello_world():
    return "Hello, World!"



# running from commandline or code
# debugging
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5555)