from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi, {name}"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    new_string = ""
    for i in range(0, num):
        new_string += name
        print(name)
    return new_string

if __name__=="__main__":
    app.run(debug=True)