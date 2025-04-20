from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Mengarahkan ke file templates/index.html
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
