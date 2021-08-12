from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/img/<number>')
def getImage(number):
    file_name = './static/' + number + '.jpg' 
    return send_file(file_name)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
