# Kamera

**Kamera** makes real-time webcam streaming effortless. The only thing you need to know is:

```bash
pip install kamera
```

```bash
kamera
```

And voilà! Your webcam is live and streaming at `http://localhost:4141`. No setup headaches, just instant results.

## Demo

![dog](https://github.com/cobanov/kamera/raw/main/assets/example.png)

## Features

- Stream live video from your webcam directly to a web interface.
- Adjust settings dynamically, including:
  - Brightness
  - Rotation
  - Grayscale
  - Mirroring
  - Filters (e.g., Sepia, Blur, Edge Detection)
- Easy-to-use API built with FastAPI.
- Real-time video processing using OpenCV.

## API Endpoints

- **GET /video_feed**: Stream the live video feed.
- **POST /settings**: Update video processing settings dynamically.

### Settings Example

Use the `/settings` endpoint to update the following parameters:

- `rotate`: Rotation angle (0, 90, 180, 270).
- `brightness`: Adjust the frame brightness (default: 1.0).
- `grayscale`: Toggle grayscale mode (default: False).
- `mirror`: Mirror the video feed (default: False).
- `filter_name`: Apply a filter (`none`, `sepia`, `blur`, `edges`).

Example request (using `curl`):

```bash
curl -X POST http://localhost:4141/settings \
  -d "rotate=90" \
  -d "brightness=1.5" \
  -d "grayscale=true" \
  -d "filter_name=sepia"
```

## License

This project is licensed under the MIT License.

---

Crafted with ❤️ by Mert Cobanov
