import cv2
import numpy as np

AVAILABLE_FILTERS = ["none", "sepia", "blur", "edges"]


def adjust_brightness(frame, brightness=1.0):
    """Adjust brightness of the frame."""
    return cv2.convertScaleAbs(frame, alpha=brightness, beta=0)


def rotate_frame(frame, angle=0):
    """Rotate the frame."""
    if angle == 90:
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(frame, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return frame


def mirror_frame(frame):
    """Mirror the frame."""
    return cv2.flip(frame, 1)


def convert_to_grayscale(frame):
    """Convert the frame to grayscale."""
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def apply_filter(frame, filter_name):
    """Apply selected filter to the frame."""
    if filter_name == "sepia":
        kernel = np.array(
            [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]
        )
        return cv2.transform(frame, kernel)
    elif filter_name == "blur":
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filter_name == "edges":
        return cv2.Canny(frame, 100, 200)
    return frame


def process_frame(
    frame, rotate=0, brightness=1.0, grayscale=False, filter_name="none", mirror=False
):
    """Apply all frame adjustments."""
    if grayscale:
        frame = convert_to_grayscale(frame)
    if mirror:
        frame = mirror_frame(frame)
    frame = adjust_brightness(frame, brightness)
    frame = rotate_frame(frame, rotate)
    frame = apply_filter(frame, filter_name)

    return frame
