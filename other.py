import cv2 as cv
import numpy as np
from numpy import array
scale = 1
raw = cv.imread('lineboard.jpg')
print '<'
raw = cv.resize(raw, (0,0), fx=1.0/scale, fy=1.0/scale)
#cv.imwrite('green.jpg', array([[x[1] for x in raw] for y in raw]))
img = cv.cvtColor(raw, cv.COLOR_BGR2GRAY)
img = 255 - img
img = (img // 190) * 255
#cv.imwrite('pic.jpg', img)

xs = []
ys = []
for y in range(len(img)):
    for x in range(len(img[0])):
        if img[y][x] > 0:
            xs.append(x)
            ys.append(y)

            


#m, b = fit(xs, ys)
m, b = np.polyfit(xs, ys, 1, full=True)[0]
print m
for x in range(len(raw[0])):
    raw[min(len(raw)-1, int(m*x + b))][x] = array([0,255,0])

print '>'
cv.imwrite('fit.jpg', cv.resize(raw, (0,0), fx=scale, fy=scale))
cv.imwrite('fit2.jpg', raw)
