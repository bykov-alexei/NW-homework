import cv2
import requests
import matplotlib.pyplot as plt
from PIL import Image

key = 'f12693bc12c7479d829a57734f145e24'
api = 'https://westeurope.api.cognitive.microsoft.com'


def find_face(img):
    plt.imsave('tmp.png', img)
    f = open('tmp.png', 'rb')
    url = api + '/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&recognitionModel=recognition_03&returnRecognitionModel=false&detectionModel=detection_02&faceIdTimeToLive=86400'
    response = requests.post(url, data=f, headers={'Ocp-Apim-Subscription-Key': key, 'Content-Type': 'application/octet-stream'})
    rect = response.json()[0]['faceRectangle']
    return rect

cap = cv2.VideoCapture('video.mp4')
width = 0
height = 0
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        rect = find_face(frame)
    except:
        continue
    if width == 0:
        width = rect['width'] * 2
        height = rect['height'] * 2
    x, y = rect['left'], rect['top']
    x, y = x - width // 4, y - height // 4
    try:
        im = Image.fromarray(frame[y:y+height, x:x+width])
    except:
        continue
    frames.append(im)

cap.release()
frames[0].save('anim.gif', save_all=True, append_images=frames[1:], optimize=False, loop=0)