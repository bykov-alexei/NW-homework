import argparse
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--img', dest='img', default='image.jpg')
parser.add_argument('--json', dest='json', default='response.json')
args = parser.parse_args()

img = plt.imread(args.img)
with open(args.json, 'r') as f:
    faces = json.load(f)

for face in faces:
    id = face['faceId']
    rectangle = face['faceRectangle']
    top, left, width, height = rectangle.values()
    cropped = img[top:top+height, left:left+width]
    plt.imsave('result/' + id + '.jpg', cropped)
