import logging
import os

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from kamera.camera import Camera


# Initialize FastAPI app
app = FastAPI()


logger = logging.getLogger("kamera")
logging.basicConfig(level=logging.INFO)

static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")

# Serve static files
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=template_path)

# Initialize camera with a dynamic index
camera = Camera()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the web interface."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video_feed")
async def video_feed():
    """Stream video frames."""

    def generate_frames():
        while True:
            frame = camera.get_frame()
            if frame is None:
                break
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    return StreamingResponse(
        generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame"
    )


@app.post("/settings")
async def update_settings(
    rotate: int = Form(0),
    brightness: float = Form(1.0),
    grayscale: bool = Form(False),
    mirror: bool = Form(False),
    filter_name: str = Form("none"),
):
    """Update camera settings dynamically."""
    camera.rotate = rotate
    camera.brightness = brightness
    camera.grayscale = grayscale
    camera.mirror = mirror
    camera.filter_name = filter_name
    logger.info("Settings updated: %s", camera.__dict__)
    return {"status": "success", "message": "Settings updated successfully"}


def main():
    uvicorn.run("kamera.app:app", host="0.0.0.0", port=4141, reload=True)


if __name__ == "__main__":
    main()
