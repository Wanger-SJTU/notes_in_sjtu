# Negative Log Likelihood Ratio Loss for Deep Neural Network Classification 

ref: [arxiv_link](https://arxiv.org/pdf/1804.10690.pdf)

## Abstract

通常的分类任务中，我们使用的是cross-entropy作为损失函数。这个等价于最大化 似然函数（**TODO**）

这篇论文则是提出了 利用NLL（负比例似然对数函数）作为损失函数来进行分类，并在`cifar-10`上做了相关实验

## LOSS FUNCTION FOR CLASSIFICATION

假设 $\mathbf{x}$ 是特征向量，$\mathbf{y}$ 是标签。我们的目标就是学习一个函数 $f(\mathbf{x})=y$ 。在实际过程中，我们是最小化期望损失函数
$$
R(f)=\mathbf{E}_{X,Y\sim  p(x,y)}L(f(x),y)
$$
这里的$L(f(x),y)$ 就是评价错分类别的损失函数. $p(x,y)$ 则是 特征空间到标签空间的概率分布,但是真实的分布是未知的。所以我们从样本中取出数据（独立同分布）得到
$$
S=\{(\mathbf{x}_1,y_1),(\mathbf{x}_2,y_2),\dots,(\mathbf{x}_m,y_m)\}
$$
此时
$$
R_s(f)=\frac{1}{m}\sum_{i=1}^m L(f(\mathbf{x}_i, y_i))
$$
在DNN 中，通常使用交叉熵作为损失函数，是因为可以依此来评价预测分布与真实分布之间的差异程度，而且可以通过SGD等算法来进行优化求解。

当最后一层经过`softmax`函数计算以后，输出即为 $\{\hat{p}(y_c|\mathbf{x}; c= 1,2,\dots,C)\}$， 此时交叉熵函数即为


$$
\begin{aligned}
L(f(\mathbf{x},y)) &= E_{p(y|\mathbf{x})}[-\log \hat{p}(y|\mathbf{x})] \\
&=-\sum_{c=1}^{C}p(y_c|\mathbf{x}) \log \hat{p}(y_c|\mathbf{x})
\end{aligned}
$$




 