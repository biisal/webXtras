"use client";
import { useState } from "react";

const DownloaderPage = () => {
    const [url, setUrl] = useState("");
    const [status, setStatus] = useState("");

    const downloadVideo = async () => {
        setStatus("Downloading...");
        try {
            const response = await fetch("http://127.0.0.1:8000/api/ytdl", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ url }),
            });            

            if (!response.ok) {
                throw new Error("Failed to download the video");
            }

            const blob = await response.blob();
            const downloadUrl = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = downloadUrl;
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
