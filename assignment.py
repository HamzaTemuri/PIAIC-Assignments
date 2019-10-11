from PIL import Image
import numpy as np
import os

np_array = np.array([])

for f in os.listdir('.'):
    if f.endswith('jpg'):
        np_array = np.append(np_array,f)

pic = Image.open(np_array[0])
pic = pic.resize((500,500))
pic.show()
pic.close()