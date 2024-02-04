# Automatic Object Outline / Border Detection

This Python script utilizes the OpenCV and rembg libraries to perform automatic object outline or border detection in an image. The script allows the user to draw a rectangle around an object in an image, then removes the background, detects contours, and overlays the contours on the original image.

## Prerequisites:
1. python
2. OpenCV('cv2')
3. rembg

Command to install libraries:
"pip install opencv-python rembg"

## Usage:
1. Ensure that you have Python installed on your machine.
2. Install the necessary libraries by running the provided pip install command.
3. Replace the image_path variable with the path to the image you want to process.
4. Run the script - "python object_outliner.py"

## Instructions
1. The script loads the specified image and resizes it to the specified width while maintaining the aspect ratio.
2. The user is prompted to draw a rectangle around the object of interest.
3. The script then removes the background from the selected region using the rembg library.
4. Contours are detected on the object.
5. The original cropped image is overlaid with the detected contours.
6. The result is displayed, allowing the user to review and make adjustments.
7. Press 'q' to exit the script.
8. Press 'c' to clear the outline and start over.
