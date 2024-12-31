import cv2

from kamera.settings import process_frame


class Camera:
    def __init__(
        self,
        rotate=0,
        brightness=1.0,
        grayscale=False,
        filter_name="none",
        mirror=False,
    ):
        self.rotate = rotate
        self.brightness = brightness
        self.grayscale = grayscale
        self.filter_name = filter_name
        self.mirror = mirror
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None
        frame = process_frame(
            frame,
            rotate=self.rotate,
            brightness=self.brightness,
            grayscale=self.grayscale,
            filter_name=self.filter_name,
            mirror=self.mirror,
        )
        _, buffer = cv2.imencode(".jpg", frame)
        return buffer.tobytes()

    def release(self):
        self.cap.release()
