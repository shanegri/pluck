#!/usr/bin/python3

import sys
import os
import yt_dlp
from moviepy.editor import *

def download_video(video_url, output_format) -> str:
    if output_format in ['mp3', 'wav', 'opus']:
        format_option = 'bestaudio/best'
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': 'best',
        }]
    elif output_format in ['mp4', 'webm']:
        format_option = f'bestvideo[ext={output_format}] + bestaudio[ext={output_format}] / best[ext={output_format}]'
        postprocessors = []
    else:
        print("Invalid output format. Supported formats: mp3, wav, opus, mp4, webm")
        sys.exit(1)

    ydl_opts = {
        'format': format_option,
        'outtmpl': '%(title)s%(ext)s',
        'postprocessors': postprocessors,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        ydl.download([video_url])
        video_title = info_dict.get('title', None)
        return f"{video_title}{output_format}"

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 yt_download.py <video_url> <output_format>")
        print("Output formats: mp3, wav, opus, mp4, webm")
        sys.exit(1)

    video_url = sys.argv[1]
    output_format = sys.argv[2]

    downloaded_file = download_video(video_url, output_format)
    print(f"File saved as: {downloaded_file}")

if __name__ == "__main__":
    main()
