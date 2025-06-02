# Some-commonly-used-small-tools
Some Python scripting tools used in work and experimental processes.

# 📽️ Image-Video Converter

A simple and efficient Python tool to:

- 🖼️ Convert a folder of images into an MP4 video.
- 🎞️ Extract every frame from an MP4 video into individual image files.

This project is useful for tasks like timelapse creation, video frame analysis, dataset generation, and basic multimedia processing using `OpenCV`.

## 🔧 Features

- Supports `.jpg`, `.jpeg`, and `.png` image formats
- Automatically sorts images before creating the video
- Outputs video in `.mp4` format using the `mp4v` codec
- Extracts all frames from a video into a specified folder
- Lightweight and easy to use — perfect for scripting and automation

## 🛠️ Requirements

- Python 3.x
- `opencv-python` package

Install via pip:

```bash
pip install opencv-python
