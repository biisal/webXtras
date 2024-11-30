from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from yt_dlp import YoutubeDL

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific domains in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary directory to store downloaded videos
TEMP_DIR = "./temp"
os.makedirs(TEMP_DIR, exist_ok=True)

# Pydantic model for video request
class VideoRequest(BaseModel):
    url: str

# Cleanup function to remove temporary files
def cleanup_file(file_path: str):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted temporary file: {file_path}")
    except Exception as e:
        print(f"Failed to delete file {file_path}: {e}")

@app.post("/api/ytdl")
def ytdl(video_request: VideoRequest, background_tasks: BackgroundTasks) -> FileResponse:
    url = video_request.url
    try:
        # Configure yt_dlp options
        ydl_opts = {
            "outtmpl": os.path.join(TEMP_DIR, "%(title)s.%(ext)s"),
            "format": "mp4/best",  # Choose the best available MP4 format
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Ensure the file exists before sending
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Video file not found")

        # Schedule file cleanup after response
        background_tasks.add_task(cleanup_file, file_path)

        # Return the video file as a response
        return FileResponse(
            file_path,
            media_type="video/mp4",
            filename=os.path.basename(file_path),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
