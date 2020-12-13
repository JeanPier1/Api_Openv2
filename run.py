from os import environ
import os
from api.app import app


# def suppress_qt_warnings():
# environ["QT_DEVICE_PIXEL_RATIO"] = "1"
# environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
# environ["QT_SCREEN_SCALE_FACTORS"] = "1"
# environ["QT_SCALE_FACTOR"] = "1"
# environ["OPENCV_VIDEOIO_DEBUG"] = "1"
# environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "1"


if __name__ == "__main__":
    port = os.environ.get("PORT") or 5000
    app.run(port=port, debug=True)
