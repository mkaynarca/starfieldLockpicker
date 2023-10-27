import cv2
import numpy as np
import math
# Load an color image in grayscale
img = cv2.imread('screenshot.png',0)
img = cv2.resize(img, (1920, 1080))
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_OTSU)

degrees = np.arange(1.5*math.pi, 3.5*math.pi, math.pi/16)

cv2.imshow('image',img)
cv2.waitKey(0)

cv2.imshow('image',blur)
cv2.waitKey(0)

cv2.imshow('image',th3)
cv2.waitKey(0)



def calculatePositions(r, x, y, degrees):
    positions = []
    for i, degree in enumerate(degrees):
        positions.append([int(y + r * np.sin(degree)), int(x + r * np.cos(degree))])
    return positions

def pointToArea(y,x, size=5):
    area = []
    for i in range(-(size-1),size):
        for j in range(-(size-1),size):
            area.append([y + i, x + j])
    return area

def pixelAreaValue(img, y, x, size=5):
    value = 0
    for i in range(-(size-1),size):
        for j in range(-(size-1),size):
            value += img[y + i][x + j]
    return value/((size+1)**2)

def findHoles(pixelAvgs:list):
    holes = []
    maxPixel = max(pixelAvgs)
    minPixel = min(pixelAvgs)
    triggerValue = (minPixel + maxPixel)*0.66
    print(f"Max: {maxPixel} Min: {minPixel} Trigger: {triggerValue}")
    for i, pixel in enumerate(pixelAvgs):
        if pixel < triggerValue:
            print(f"{i} - {pixel:<.2f} Eklendi")
            holes.append(i)
        else:
            print(f"{i} - {pixel:<.2f} Eklenmedi")
    print("")
    print("")
    print("")
    return holes

x_lock = 960
y_lock = 540

r_locks = [204, 167, 135, 105]

for r_lock in r_locks:
    pixelAvg = []
    positions = calculatePositions(r_lock, x_lock, y_lock, degrees)
    for position in positions:
        pixelAvg.append(pixelAreaValue(blur, position[0], position[1]))
        colorArea = pointToArea(position[0], position[1])
    
    holes = findHoles(pixelAvg)
    for hole in holes:
        position = positions[hole]
        holePos = pointToArea(position[0], position[1])
        for pos in holePos:
            img[pos[0]][pos[1]] = 255
            
cv2.imshow('image',img)
cv2.waitKey(0)