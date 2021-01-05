from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test1')
def test1():
    return '{"message": "Test Response 1"}'


@app.route('/test2')
def test2():
    return '{"message": "Test Response 2"}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15274, debug=True)
