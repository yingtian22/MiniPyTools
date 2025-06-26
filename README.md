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

# 📊 Image to 3D Surface Plot

将任意灰度图像转换为三维表面图（3D surface plot），并保存为高质量图像。  
适用于图像可视化、图像处理教学演示、学术论文图表制作等专业场景。

---

## 📌 特性

- ✅ 将图像像素强度映射为 3D 高度信息  
- 🎨 专业美术风格（Times New Roman 字体、柔和配色、白色背景）  
- 🖼️ 自定义渐变 colormap（深蓝 → 白）  
- 📈 高分辨率图像输出，适用于论文插图  
- 🧠 支持任意图像格式，自动转为灰度处理  

---

## 🖼️ 可视化示例

> 运行后会生成类似如下的图像：

<p align="center">
  <img src="surface_plot.png" alt="3D surface plot example" width="600">
</p>

---

## 📦 安装依赖

```bash
pip install numpy matplotlib pillow
```

```bash
from plot_3d import plot_3d_surface

# 调用函数，生成 3D 表面图
plot_3d_surface('your_image.png', 'output_3d_plot.png')
```

# 📈 Grayscale Histogram Plotter

该工具可将任意图像（自动转换为灰度）转换为平滑处理的像素强度直方图，并输出为高质量学术风格图像。  
适用于图像分析、计算机视觉教学、科研论文图表等场景。

---

## 🎯 功能特性

- 自动读取图像并转换为灰度模式
- 生成平滑处理的灰度直方图（支持高斯滤波）
- 支持绘制像素强度均值线与标准差区域
- 使用对数纵轴更好展示图像分布特性
- 输出专业风格图表，默认字体为 Times New Roman

---

## 🖼️ 输出图示

> 运行后将生成如下所示的直方图：

<p align="center">
  <img src="histogram.png" alt="Grayscale Histogram Example" width="600">
</p>

---

## 📦 安装依赖

```bash
pip install opencv-python matplotlib scipy numpy
```
```bash
from histogram_plot import plot_histogram

plot_histogram('your_image.png', 'output_histogram.png')
```
