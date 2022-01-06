from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def post():
    return {"Status": "Post correct!!"}


if __name__ == '__main__':
    app.run('localhost', port=5454)