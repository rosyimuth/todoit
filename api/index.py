from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask & Vercel!'

# Fungsi wajib untuk Vercel agar bisa menjalankan app
def handler(environ, start_response):
    return app(environ, start_response)
