from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Wajib! Agar Vercel tahu fungsi handler-nya
def handler(environ, start_response):
    return app(environ, start_response)
