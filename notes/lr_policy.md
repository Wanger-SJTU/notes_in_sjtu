# learning rate四种改变方式

## 1. Fixed

固定不变

## 2. step

随着步长变化

learning rate在每迭代step size次后减少 $\gamma$ 倍。$lr=lr×\gamma $

## 3.Polynomial（多项式）

learning rate呈多项式曲线下降。  $LR(t)=base\_lr\times(\frac{t}{T})^{power}$

##  4.Inv

learning rate随迭代次数增加而下降。 $LR(t)=base\_lr\times(1+gamma\times iter)^{power}$