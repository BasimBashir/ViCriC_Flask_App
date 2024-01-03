from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/user_uploads'


@app.route('/', methods=['GET'])
def upload():
    return render_template('Upload.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_files = request.files.getlist('files')
    for file in uploaded_files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('upload'))


@app.route('/pitchMap')
def drawMap():
    return render_template('pitch.html')


@app.route('/save_point', methods=['POST'])
def pitchmap():
    data = request.json
    # Process and save the received point data as needed
    print('Received point:', data)
    return redirect(url_for('drawMap'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('Dashboard.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
