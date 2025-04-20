from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/', methods=['GET', 'POST'])
def todoit():
    if request.method == 'POST':
        data = request.form['data']  # Menangkap data yang dikirim
        # Mengirim data ke template untuk ditampilkan
        return render_template('index.html', data=data)
    return render_template('index.html', data=None)  # Jika GET, kirim None untuk data
