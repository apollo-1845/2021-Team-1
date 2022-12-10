from picamera import PiCamera
from time import sleep
from PIL import Image
from PIL import ImageOps
from io import BytesIO
from sense_hat import SenseHat
from orbit import ISS
from skyfield.api import load

# Initialize all the things
sense = SenseHat()
camera = PiCamera()
camera.resolution = (2592, 1944)


for i in range(360):
    # Capture magnetometer readings
    raw = sense.get_compass_raw()
    with open("magnetometerReadings.csv", "a") as f:
        f.write(str(raw["x"]) + ", " + str(raw["y"]) + "," + str(raw["z"]) + "\n")
    
    
    # Capture camera images
    img = BytesIO()
    camera.capture(img, format='jpeg')
    img.seek(0)
    img = Image.open(img)
    img = ImageOps.grayscale(img)
    img.save(f'image_{i:03d}.jpg')
    
    
    # Capture current ISS location
    time = load.timescale().now()
    position = ISS.at(time)
    location = position.subpoint()
    with open("locations.txt", "a") as locations:
        locations.write(f"{location}\n")
    
    sleep(30)
