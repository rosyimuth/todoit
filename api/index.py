from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask & Vercel!"

# WAJIB ada untuk Vercel:
def handler(environ, start_response):
    return app(environ, start_response)
