from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, 我的第一个工程化项目!"

if __name__ == '__main__':
    app.run(debug=True)