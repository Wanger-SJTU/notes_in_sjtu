# loss function in pytorch

## Cross Entropy(交叉熵)

交叉熵越小，就证明算法所产生的策略越接近最优策略，也就间接证明我们的算法所计算出的非真实分布越接近真实分布

 交叉熵损失函数从信息论的角度来说，其实来自于KL散度，只不过最后推导的新式等价于交叉熵的计算公式：

H(p,q)=−∑k=1N(pk∗logqk)H(p,q)=−∑k=1N(pk∗logqk)

**最大似然估计、Negative Log Liklihood(NLL)、KL散度与Cross Entropy其实是等价的**，都可以进行互相推导，当然MSE也可以用Cross Entropy进行对到出（详见Deep Learning Book P132）。