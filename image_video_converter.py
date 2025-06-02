import cv2
import os

def images_to_video(image_folder, output_video_path, fps=30):
    images = sorted([
        img for img in os.listdir(image_folder)
        if img.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])
    
    if not images:
        print("No images found.")
        return

    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for image_name in images:
        img_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Failed to read image: {img_path}")
            continue
        video.write(frame)

    video.release()
    print(f"Video saved to {output_video_path}")

def video_to_images(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Failed to open video file.")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        image_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(image_path, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

# Example usage:
# images_to_video("path/to/image_folder", "output_video.mp4")
# video_to_images("input_video.mp4", "path/to/output_frames")
