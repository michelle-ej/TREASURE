# import os
# import glob
# import cv2
# # os.chdir('../../../../../picture-testing')
# # print(os.getcwd())
# # print(glob.glob("*.jpg"))
# filename = 'C:/Users/USER/Desktop/treasure507/picture-testing/'
# files= os.listdir(filename)
# for file in files:
    
import fnmatch, os
path='C:/Users/USER/Desktop/treasure507/picture-testing/'
exts = ['*.jpg']
matches = []
for root, dirs, files in os.walk(path):
    for ext in exts:
        for file in fnmatch.filter(files,ext):
            matches.append(os.path.join(root, file))
for image in matches:
    print(image)