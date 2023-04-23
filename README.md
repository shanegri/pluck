# Pluck

Pluck is a command-line tool for downloading videos and audios from YouTube using `yt-dlp` and `moviepy` Python libraries. Note that Pluck also depends on `ffmpeg`.

## Install

You can install Pluck by cloning the repository and installing the dependencies:

```sh
git clone https://github.com/shanegri/pluck.git
cd pluck
pip install -e .
```

This will install `yt-dlp` and `moviepy` alongside other required dependencies.

Additionally, you need to have `ffmpeg` installed on your system. You can install it using your system's package manager, or download a binary from the official [FFmpeg website](https://ffmpeg.org/download.html).

Note that Pluck only supports Python 3.

## Run

To download a video or audio, you can run the `pluck` command followed by the YouTube URL and output format:

```sh
pluck <video_url> <output_format>
```

Alternatively, you can run the script directly:

```sh
python pluck/pluck.py <video_url> <output_format>
```

Supported output formats are: `mp3`, `wav`, `opus`, `mp4`, and `webm`.

## Tests

You can run the tests for Pluck using the following command:

```sh
python -m unittest discover -s tests
```

The tests cover basic functionality, such as downloading videos and audios and handling invalid formats.

