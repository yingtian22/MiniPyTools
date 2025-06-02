# 🧰 MiniPyTools

A curated collection of small but handy Python scripting tools used in daily work, automation, and experimental workflows.

These tools are lightweight, reusable, and easy to extend for various tasks such as file processing, data cleaning, image analysis, and system scripting.

> Some commonly used small Python tools for real-world productivity and research support.


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
```

## 🚀 Usage

### 1. Convert a folder of images to an MP4 video

```python
from image_video_converter import images_to_video

# Example: Create a video from images in 'image_folder', save as 'output_video.mp4'
images_to_video("image_folder", "output_video.mp4", fps=30)
```

# 🖼️ Image Resizer

A simple Python tool to batch resize images in a folder to a specific width and height (m × n).

Ideal for preprocessing datasets, standardizing image sizes for ML tasks, or simply resizing multiple images at once.

## 🔧 Features

- Batch resize `.jpg`, `.jpeg`, and `.png` images
- Customize output size with height (`m`) and width (`n`)
- Saves resized images to a separate output folder
- Uses `OpenCV` for fast and reliable image processing

## 🛠️ Requirements

- Python 3.x
- `opencv-python` package

Install with:

```bash
pip install opencv-python
```

## 🚀 Usage

### Import and Call the Function

```python
from image_resizer import resize_images

# Example: Resize all images in 'input_folder' to 256x256 and save them to 'resized'
resize_images("input_folder", "resized", 256, 256)
```
