[TOC]

## loss函数

损失函数是为了衡量当前参数下model的预测值predict距离真实值label的大小。通过模型得到的predictions服从一个分布，而目标标签也符合一个分布。损失函数即衡量两个分布的距离，或者说相似程度。如果两个分布的相似度越大，则有损失函数的数值越小。

不直接使用评价指标的原因：

- 可微性不一定满足。
- 映射到的函数空间不一定具有可分性。？？

## 似然函数

通用的定义来说，似然函数就是衡量当前模型参数对于已知样本集的解释情况，通用的表现形式如下：$L=P(X;\theta)$。 似然函数的定义当然没有限定样本集$X$的分布函数。

我们将似然函数作为机器学习模型的损失函数，并且用在分类问题中

似然函数是直接作用于模型的输出的，所以对于似然函数来说，这里的样本集就成了label集（而不是机器学习意义上的样本集X了），这里的参数也不是机器学习model 的参数，而是predict值！

**即作为损失函数的似然函数，衡量了样本标签与预测值的分布距离**

[refer](https://zhuanlan.zhihu.com/p/27719875)

## 常用loss

