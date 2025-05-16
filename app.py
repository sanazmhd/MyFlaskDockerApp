from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return 'Hello Sanaz,Welcom to your new Docker Flask App!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
