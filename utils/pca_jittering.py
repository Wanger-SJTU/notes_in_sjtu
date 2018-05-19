import numpy as np
import os
from PIL import Image, ImageOps
import argparse
import random
from scipy import misc

def main():
  img_num = len(os.listdir(args.root_dir + '/'+args.dataset))

  for i in range(img_num):
    img_name = os.listdir(args.root_dir + '/'+args.dataset)[i]
    img = Image.open(os.path.join(args.root_dir,args.dataset,img_name))
    img = np.asarray(img, dtype='float32')

    img = img /255.
    img_size = img.size/3
    img1=img.reshape(img_size,3)
    img1=np.transpose(img1)
    img_conv = np.cov([img1[0],img1[1],img1[2]])
    l,p = np.linalg.eig(img_conv)

    p=np.transpose(p)

    alpha1 = random.normalvariate(0, 0.3)
    alpha2 = random.normalvariate(0, 0.3)
    alpha3 = random.normalvariate(0, 0.3)
    v = np.transpose((alpha1*l[0],alpha2*l[1],alpha3*l[2]))

    add_num = np.dot(p,v)

    img2 = np.array([img[:,:,0]+add_num[0],img[:,:,1]+add_num[1],img[:,:,2]+add_num[2]])

    img2 = np.swapaxes(img2, 0, 2)
    img2 = np.swapaxes(img2, 0, 1)
  misc.imsave('./out/test.jpg',img2)