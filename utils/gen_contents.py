
import os
import os.path as osp

here = osp.dirname(osp.abspath(__file__))
root = osp.join(here, '..')

def skip_dir(path):
  skip_dir_name = ['.git', 'pic']
  for item in skip_dir_name:
    if item in path:
      return True
  return False

for item in os.walk(root):
  if not skip_dir(item[0]):
    print(item[0])

