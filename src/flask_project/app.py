from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, 我的第一个工程化项目!"

@app.route('/about')
def about():
    return "我是ZhuanZ，这是我的第一个独立完成的工程页面！"

if __name__ == '__main__':
    app.run(debug=True)