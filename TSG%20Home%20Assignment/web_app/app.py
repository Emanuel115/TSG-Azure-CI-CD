from flask import Flask
import os

app = Flask(__name__)
secret = os.getenv("SUPER_SECRET", "No Secret Set")

@app.route('/')
def hello():
    return f"Hello, your secret is: {secret}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
