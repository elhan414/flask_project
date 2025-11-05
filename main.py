from flask import Flask


aap = Flask(__name__)
@aap.route('/')

def hello():
    return 'Hello World!'

if __name__ == '__name__':
    aap.run(debug=True)