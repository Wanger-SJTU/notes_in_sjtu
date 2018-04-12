[TOC]

## ImportError: cannot import name X

1. 问题描述

   在 `data_utils.py`中有

```python
import numpy as np
from PIL import Image
```

在`GTA5.py`中

```python
import torch
import os
import sys
import collections
import os.path as osp
import numpy as np 
import scipy.io as sio

from PIL import Image as image
from torch.utils import data

from data.data_utils import get_num_classes
from data.data_utils import resize_input
```

报错信息

> Traceback (most recent call last):
>   File "train.py", line 10, in <module>
>     from data.GTA5 import GTA5
>   File "C:\Users\chmtt\Desktop\fcn-in-the-wild\data\GTA5.py", line 15, in <module>
>     from data.data_utils import resize_input
> ImportError: cannot import name 'resize_input'

原因

> 在两个文件中，PIL.Image引用的两个名称不一致冲突