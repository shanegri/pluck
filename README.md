# Pluck

Pluck is a command-line tool for downloading videos and audios from YouTube using `yt-dlp` and `moviepy` Python libraries.

## Install

You can install Pluck by cloning the repository and installing the dependencies manually:

```sh
git clone https://github.com/your-username/pluck.git
cd pluck
pip install -r requirements.txt
```

Alternatively, you can use the following command to install Pluck in "editable" mode, which links the local copy of the repository to your Python environment:

```sh
pip install -e .
```

Note that Pluck only supports Python 3.

## Run

To download a video or audio, run the `pluck` command followed by the YouTube URL and output format:

```sh
python pluck/pluck.py <video_url> <output_format>
```

The supported output formats are: `mp3`, `wav`, `opus`, `mp4`, and `webm`.

## Tests

You can run the tests for Pluck using the following command:

```sh
python -m unittest discover -s tests
```

The tests cover basic functionality, such as downloading videos and audios and handling invalid formats.