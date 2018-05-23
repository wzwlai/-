from flask import Flask


app = Flask(__name__)



@app.route('/')
def lai():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)
gaiagaer