- 导出python 项目的requirements.txt

  对于使用anaconda，每个项目建一个虚拟环境的可以直接使用`pip freeze >> requirements.txt`来导出。

  但是如果没有这个习惯，或者是不是anaconda的用户，可以使用`pipreqs`包来完成。

  ```python
  # 使用方式也比较简单
  # 在项目根目录
  pipreqs ./
  ```

  ​

- ​