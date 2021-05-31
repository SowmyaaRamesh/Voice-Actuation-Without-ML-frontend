import os
from flask import Flask,render_template,request
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\')


@app.route('/')
def upload_image():
    return render_template('index.html')


@app.route('/uploadAudio',methods=['POST'])
def image_upload():
    f = request.files['audioFile']
    f.save(os.path.join(UPLOADS_PATH,f.filename))
    word = request.form['word']
    print(word)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()