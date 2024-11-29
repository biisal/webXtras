"use client";
import { useState } from "react";
import axios from "axios";

const DownloaderPage = () => {
    const [url, setUrl] = useState("");
    const [status, setStatus] = useState("");

    const downloadVideo = async () => {
        setStatus("Downloading...");
        try {
            const response = await axios.post(
                "http://127.0.0.1:5000/api/download",
                { url },
                { responseType: "blob" } // To handle file responses
            );

            const urlBlob = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement("a");
            link.href = urlBlob;
            link.setAttribute("download", "video.mp4");
            document.body.appendChild(link);
            link.click();
            link.remove();

            setStatus("Download successful!");
        } catch (error) {
            console.error(error);
            setStatus("Failed to download video.");
        }
    };

    return (
        <div className="flex flex-col items-center justify-center p-4">
            <h1 className="text-2xl font-bold">YouTube Video Downloader</h1>
            <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter YouTube URL"
                className="border p-2 m-4 w-full max-w-md"
            />
            <button
                onClick={downloadVideo}
                className="bg-blue-500 text-white px-4 py-2 rounded"
            >
                Download
            </button>
            {status && <p className="mt-4">{status}</p>}
        </div>
    );
};

export default DownloaderPage;
