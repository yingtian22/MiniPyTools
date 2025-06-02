import cv2
import os

def resize_images(input_folder, output_folder, target_height, target_width):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_exts = ('.jpg', '.jpeg', '.png')
    images = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_exts)]

    if not images:
        print("No images found in the input folder.")
        return

    for img_name in images:
        input_path = os.path.join(input_folder, img_name)
        output_path = os.path.join(output_folder, img_name)

        image = cv2.imread(input_path)
        if image is None:
            print(f"Failed to load image: {input_path}")
            continue

        resized_image = cv2.resize(image, (target_width, target_height))
        cv2.imwrite(output_path, resized_image)
        print(f"Saved resized image to: {output_path}")

    print("All images have been resized.")

# Example usage:
# resize_images("input_folder", "resized_folder", m, n)
