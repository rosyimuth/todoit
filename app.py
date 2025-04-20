from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def todoit():
    if request.method == 'POST':
        data = request.form['data']
        return render_template('index.html', data=data)
    return render_template('index.html', data=None)