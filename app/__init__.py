from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return "Hello World!"

@app.route('/minky')
def minky():
    return 'minky moodle'

if __name__ == "__main__":
    app.run()

