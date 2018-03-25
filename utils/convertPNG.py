
import numpy as np


def index2rgb(indexed, palette):
  w, h = indexed.shape
  rgb_img = np.zeros((w, h, 3))

  for i in range(len(palette)):
    mask = indexed == i
    rgb_img[mask] = 255 - palette[i]

  return rgb_img