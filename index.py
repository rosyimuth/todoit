from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Menggunakan render_template untuk merender file templates/index.html
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
