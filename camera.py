from picamera import PiCamera
from time import sleep
from PIL import Image
from PIL import ImageOps
from io import BytesIO


camera = PiCamera()
camera.resolution = (2592, 1944)



for i in range(360):
    stream = BytesIO()
    img = camera.capture(stream, format='jpeg')
    img.seek(0)
    img = Image.open(img)
    img = ImageOps.grayscale(img)
    img.save(f'image_{i:03d}.jpg')
    
    sleep(30)
