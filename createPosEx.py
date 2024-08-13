import cv2 as cv
import os

ch = "betty"

f = open(f'antrenare/{ch}_annotations.txt', "r")
i = 1
for det in f:
    a = det.split()
    image_no = a[0]
    x_min = int(a[1])
    y_min = int(a[2])
    x_max = int(a[3])
    y_max = int(a[4])

    img = cv.imread(os.path.join(f'antrenare/{ch}', image_no), cv.IMREAD_GRAYSCALE)
    img = img[y_min:y_max, x_min:x_max]
    img = cv.resize(img, (36, 36))
    cv.imwrite(f'data/exemplePozitive3636/{ch}{str(i).zfill(4)}.jpg', img) 

    i += 1