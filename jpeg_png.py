"""
This code was
"""


from PIL import Image
import os
import sys
from time import time

start = time()

#take tro arguments from terminal one the dir that contain jpg files and the one you want to save
files_dir = sys.argv[1]
new_dir = sys.argv[2]


#create the new dir. But only if it doesnt exist
if not(os.path.isdir(new_dir)):
    os.mkdir(new_dir)



#save the pictures as array
arr = os.listdir(files_dir)


for file in arr:
	if '.jpg' in file:
		index = file.index('.')
		name = file[:index]
		img = Image.open(str(files_dir)+str(file))
		img.save('./'+str(new_dir)+str(name)+'.png')
		

run_time = time() - start		
print("it took {0} seconds".format(run_time))