## No module named 'utils.util'; 'utils' is not a package

出错不扽源代码为

```python
from utils.util import label_accuracy_score
from data.utils import get_num_classes
from data.utils import index2rgb
```

原相关目录结构为

```

├── data
│   ├── utils.py
│   ├── GTA5
│   │   ├── train
│   │   │   ├── images
│   │   │   ├── labels
│   │   └── val
│   │       ├── images
│   │       ├── labels
│   ├── GTA5.py
│   ├── __init__.py
└── utils
    ├── __init__.py
    ├── transform.py
    └── util.py
```

主要报错信息为

```
ModuleNotFoundError:     No module named 'utils.util'; 'utils' is not a package
```

原因

> 同一文件引用中应该是不能出现名字相同的package名称。
>
> 在引用中 utils.util 和data.utils 冲突

解决方法

> 将其中一个改名，不冲突。或者重新组织目录结构。

```python
from utils.util import label_accuracy_score
from data.data_utils import get_num_classes
from data.data_utils import index2rgb
```

```
├── data
│   ├── data_utils.py
│   ├── GTA5
│   │   ├── train
│   │   │   ├── images
│   │   │   ├── labels
│   │   └── val
│   │       ├── images
│   │       ├── labels
│   ├── GTA5.py
│   ├── __init__.py
└── utils
    ├── __init__.py
    ├── transform.py
    └── util.py
```

