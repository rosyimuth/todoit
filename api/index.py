from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello from Flask on Vercel!"})

def handler(environ, start_response):
    # Pastikan app.wsgi_app yang digunakan untuk handler
    return app.wsgi_app(environ, start_response)
