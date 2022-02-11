import cv2
import glob
import os

images = glob.glob("../files/sample_images/*.jpg")
files = [f.split("/")[3] for f in images]
file_path_dest = '/Users/cenkakdeniz/Desktop/projects/python/pythonTutorial/files/resized_images/'

for image in images:
    file_name = 'resized_'+image
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (500, 500))
    cv2.imshow("GALAXY", re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    ret = cv2.imwrite(file_path_dest+image.split("/")[3], re)
    print(ret, os.path.join(file_path_dest, image.split("/")[3]))