import cv2


def take_picture(file_name="temp.jpg"):
    """
    Takes a picture using the default camera and saves it to a file.

    Args:
        file_name (str): Name of the output image file.
    """
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Camera initialized. Press SPACE to take a picture or ESC to exit.")

    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Could not capture frame.")
            break

        # Display the frame
        cv2.imshow('Camera', frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        # If ESC is pressed, exit
        if key == 27:  # ESC key
            print("Exiting without taking picture...")
            break

        # If SPACE is pressed, take picture
        elif key == 32:  # SPACE key
            cv2.imwrite(file_name, frame)
            print(f"Picture saved as {file_name}")
            break

    # Release everything
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        file_name = input(
            "Enter the output file name (default: photo.jpg): ") or "photo.jpg"
        take_picture(file_name)
    except Exception as e:
        print("An error occurred:", e)
