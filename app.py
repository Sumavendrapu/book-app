from flask import Flask

app = Flask(__name__)

books = [
    "Python Basics",
    "Docker Fundamentals and volumes",
    "DevOps Handbook"
]

@app.route('/')
def home():
    return {
        "books": books
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)