from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()

camera.start_preview()
sleep(2)

camera.capture(stream, format='jpeg')

# 내용을 읽기위해 스트림을 되감기함(rewind)
stream.seek(0)  # 쓰기하고 처음부터 내용을 읽기 위해 사용

image = Image.open(stream)
image.show()
