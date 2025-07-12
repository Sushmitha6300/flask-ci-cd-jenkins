from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Hello from Sushmitha's Flask App running on Docker with Jenkins CI/CD!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
