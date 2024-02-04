# Task 1: Automatic Object Outline /Border Detection

import cv2
from rembg import remove

def process_image(image_path, new_width=800):
    # Read the original image
    original_image = cv2.imread(image_path)

    # Resize the original image to the specified width (maintaining aspect ratio)
    aspect_ratio = original_image.shape[1] / original_image.shape[0]
    new_height = int(new_width / aspect_ratio)
    resized_image = cv2.resize(original_image, (new_width, new_height))

    # Convert the resized image to RGBA format (if not already)
    if resized_image.shape[2] == 3:
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2BGRA)

    # Create a copy of the resized image for processing
    processed_image = resized_image.copy()

    while True:
        # Resize the processed image for display
        display_image = cv2.resize(processed_image, (400, 400))  # Adjust display size as needed

        # Display the resized image
        cv2.imshow("Image", display_image)

        # Ask the user to draw a rectangle
        roi = cv2.selectROI("Image", processed_image, showCrosshair=True, fromCenter=False)
        x, y, w, h = roi

        if w and h:
            # Crop the ROI from the processed image
            cropped_image = processed_image[y:y+h, x:x+w]

            # Remove the background using rembg library
            cropped_image_no_bg = remove(cropped_image)

            # Find contours
            gray = cv2.cvtColor(cropped_image_no_bg, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw contours on the original cropped image
            for cnt in contours:
                cv2.drawContours(cropped_image, [cnt], 0, (0, 255, 0), 2)

            # Overlay the contour image on the processed image
            processed_image[y:y+h, x:x+w] = cv2.resize(cropped_image, (w, h))

        # Display the result
        cv2.imshow("Result", cv2.resize(processed_image, (400, 400)))

        # Wait for the user input
        key = cv2.waitKey(0)

        if key == ord('q'):
            break
        elif key == ord('c'):
            # Clear the outline
            processed_image = resized_image.copy()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "2.jpg"  # image path
    process_image(image_path)
