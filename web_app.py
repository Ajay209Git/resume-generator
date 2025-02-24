from flask import Flask, request, render_template, send_file
from app import download_youtube_video_as_mp3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_path = 'downloads'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    mp3_file = download_youtube_video_as_mp3(url, output_path)
    return send_file(mp3_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)