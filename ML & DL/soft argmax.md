## A soft argmax

在推断过程中，我们经常使用argmax来计算预测的label。但是这个不可导的，不能得到梯度值。因此就需要一个可导的函数，来近似求解。

我们知道`softmax`函数为
$$
\text{softmax}(x)=\frac{e^{x_i}}{\sum_j e^{x_j}}
$$
通过softmax函数可以得到归一化的概率值。但这个可能值还是太小了。


$$
\text{soft-argmax}(x)=\sum_i\frac{e^{\beta x_i}}{\sum_j e^{\beta x_j}}i
$$
$\beta$s是任意大的一个值