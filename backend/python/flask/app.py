from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from yt_dlp import YoutubeDL

app = Flask(__name__)
CORS(app)

# Temporary directory to store downloaded videos
TEMP_DIR = "./temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route('/api/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({"error": "Missing 'url' in request body"}), 400

        url = data['url']
        print(f"Downloading video: {url}")

        # Define output template and options for yt_dlp
        output_template = os.path.join(TEMP_DIR, "%(title)s.%(ext)s")
        ydl_opts = {
            'outtmpl': output_template,
            'format': 'bestvideo+bestaudio/best',  # Best quality
            'merge_output_format': 'mp4',         # Ensure MP4 output
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Return the video file as a response
        return send_file(
            file_path,
            as_attachment=True,
            download_name=os.path.basename(file_path),
            mimetype="video/mp4"
        )
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
