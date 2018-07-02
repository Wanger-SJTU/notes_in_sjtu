



## 输出矢量图

```python
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```

其实 `Jupyter Notebook` 上面输出的是不是矢量图还无所谓，最重要的是生成的插图不能糊啊。`savefig` 只要指定文件名后缀是` .pdf` 或者` .eps` 就能生成能方便地插入 `latex` 的图片了！ 

```python
plt.savefig('tmp.pdf', bbox_inches='tight')
plt.show()
```

