# Some of this was grabbed from the Aldebaran documentation

from naoqi import ALProxy
import vision_definitions
import time
from PIL import Image

IP = "131.181.46.176" 
PORT = 9559

print "VIDEO PROXY COMING UP ON: ", IP
camProxy = ALProxy("ALVideoDevice", IP, PORT)

# Register generic vid model
resolution = vision_definitions.kQQVGA
colorSpace = vision_definitions.kYUVColorSpace
fps = 20

nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

print 'GRAB IMAGEREMOTE'


for i in range(0, 20):
  print "getting image " + str(i)
  naoImage = camProxy.getImageRemote(nameId)

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  print "We got width: %s, height: %s" % (imageWidth, imageHeight)

  im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
  
  # Save the image.
  imname = "camImage%d.png" % i
  print imname
  im.save(imname, "PNG")
  print "done!"
  time.sleep(0.8)

# Shut this bad boy down
camProxy.unsubscribe(nameId)

