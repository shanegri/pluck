import os
import unittest
from pluck.pluck import download_video

FIRST_YT_VIDEO = "https://www.youtube.com/watch?v=OaGwyCSw0bo"

class TestYTDownload(unittest.TestCase):

    def test_download_audio(self):
        video_url = FIRST_YT_VIDEO
        output_format = "mp3"
        downloaded_file = download_video(video_url, output_format)
        self.assertTrue(os.path.exists(downloaded_file), downloaded_file)
        os.remove(downloaded_file)

    def test_download_video(self):
        video_url = FIRST_YT_VIDEO
        output_format = "mp4"
        downloaded_file = download_video(video_url, output_format)
        self.assertTrue(os.path.exists(downloaded_file), downloaded_file)
        os.remove(downloaded_file)

    def test_invalid_format(self):
        video_url = FIRST_YT_VIDEO
        output_format = "invalid_format"
        with self.assertRaises(SystemExit):
            download_video(video_url, output_format)


if __name__ == "__main__":
    unittest.main()
