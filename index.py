from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def todoit():
    if request.method == 'POST':
        # Jika ada data yang dikirim melalui metode POST
        data = request.form.get('some_data')
        # Lakukan sesuatu dengan data yang diterima
        return f"Data yang dikirim: {data}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
