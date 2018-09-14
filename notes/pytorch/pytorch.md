[TOC]

# 删除网络的最后一层

```python
self.features =  nn.Sequential(*list(model.features.children()) + list(model.classifier.children())[:-1])  
```

以alexnet为例。 load进来的模型 分为两部分`model.features`和`model.classifier`

# DEBUG

> ```bash
> RuntimeError: cuda runtime error (59) : device-side assert triggered at /opt/conda/conda-bld/pytorch_1524580978845/work/aten/src/THC/generic/THCStorage.c:36
> ```

