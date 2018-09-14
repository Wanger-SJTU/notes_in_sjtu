#PILCO

[refer-1](https://blog.csdn.net/philthinker/article/details/79749038)

[refer-2](https://zhuanlan.zhihu.com/p/27539273)

### model based

一般来讲，所谓基于模型的强化学习是指先从数据中学习模型，然后基于学到的模型对策略进行优化。如果模型完全已知了，其实就变成了最优控制问题。从数据中学习模型的本质其实是提高了数据的利用效率。因为利用已有的数据学到系统的模型后，利用这个模型你就可以预测其他未知状态处的值了。 

基于模型的强化学习算法最大的缺点是不具有通用性。因为很多情况下系统无法建模，如游戏或者自然语言处理等。但是有的情况系统是有模型的。比如机器人系统的运动。机器人系统的运动符合最基本的物理定律。利用发展起来的刚体、流体等动力学可以对这些系统进行建模。所以，像机器人系统的运动这类问题比较适合于基于模型的强化学习方法（当然无模型的强化学习方法也可以解决，如DDPG等）。 

###**基于模型强化学习方法最大的挑战：模型误差**

基于模型强化学习方法最大的缺点是通过数据学习到的模型存在模型误差。尤其是刚开始的时候，数据很少，利用很少的数据学到的模型必定不准确。利用不准确的模型去预测未知状态的值便会产生更大的误差。

**PILCO**

将模型误差考虑进去的基于模型的强化学习算法是PILCO。PILCO一般只需要几次到几十次便可以成功实现对单摆等典型非线性系统的稳定性控制，而对于同样的问题，基于无模型的强化学习则需要上万次。

**PILCO** **的成功关键是：**

PILCO解决模型偏差的方法不是集中于一个单独的动力学模型，而是建立了概率动力学模型，即动力学模型上的分布。也就是说，PILCO建立的模型并不是具体的某个确定性函数，而是建立一个可以描述一切可行模型（所有通过已知训练数据的模型）上的概率分布。该概率模型有两个目的：

第一， 它表达和表示了学习到的动力学模型的不确定性

第二， 模型不确定性被集成到了长期的规划和决策中。

## PILCO 算法

![1531833814984](./pics/1531833814984.png)

**底层**：学习一个状态转移的概率模型

**中间层**：利用状态转移的概率模型和策略$\pi$，预测在策略$\pi$下，后续的状态分布$p(x_0),p(x_1),...,p(x_T)$ ，利用$V^{\pi}(x_0)=\sum_{t=0}^T\int c(x_t)p(x_t)dx_t$对策略进行评估.

**顶层**：在顶层利用基于梯度的方法对策略$\pi$的参数进行更新。

####  **底层：学习转移概率模型**

PILCO算法用的概率模型是高斯过程模型。

该部分的相关数学基础可在如下资料中找到：

> 《Gaussian Processes for Machine Learning》
>
> 《State Estimation for Robotics》

假设动力学系统可以由下列公式描述 
$$
x_t=f(x_{t-1},u_{t-1})
$$
PILCO的概率模型并不对该模型直接进行建模，而是引入了一个差分变量![\Delta_t](http://www.zhihu.com/equation?tex=%5CDelta_t)，通过如下变换 
$$
\Delta_t=x_t-x_{t-1}+\epsilon
$$
设$\Delta_t$符合高斯分布，则![x_t](http://www.zhihu.com/equation?tex=x_t)也符合高斯分布：
$$
p(x_t|x_{t-1},u_{t-1})=\mathcal{N}(x_t|\mu_t, \Sigma_t)
$$


其中均值：

![\[ \mu_t=x_{t-1}+E_f\left[\Delta_t\right] \]](http://www.zhihu.com/equation?tex=%5C%5B+%5Cmu_t%3Dx_%7Bt-1%7D%2BE_f%5Cleft%5B%5CDelta_t%5Cright%5D+%5C%5D) (1.3)

令![\widetilde{x}=\left(x,u\right)](http://www.zhihu.com/equation?tex=%5Cwidetilde%7Bx%7D%3D%5Cleft%28x%2Cu%5Cright%29)，PILCO动力学概率模型学习的是输入![\widetilde{x}](http://www.zhihu.com/equation?tex=%5Cwidetilde%7Bx%7D)和输出![\Delta](http://www.zhihu.com/equation?tex=%5CDelta)之间的拟合关系。跟直接学习函数值相比，学习差分更有优势。因为相比于原来的函数，它们的变化很少。学习差分![\Delta x](http://www.zhihu.com/equation?tex=%5CDelta+x)近似于学习函数的梯度。

