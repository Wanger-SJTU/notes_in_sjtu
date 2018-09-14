

# Deep Lab V3+

[**Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation** ](https://arxiv.org/abs/1802.02611)



结构如下：

![preview](https://pic3.zhimg.com/v2-03f33d1270a6e20cc8b3202e5cc5372a_r.jpg) 

## Xception[1]

在一层卷积中我们尝试训练的是一个 3-D 的 kernel，kernel 有两个 spatial dimension，H 和 W，一个 channel dimension，也就是 C。 这样一来，一个 kernel 就需要同时学习 spatial correlations 和 cross-channel correlations，我把这里理解为，spatial correlations 学习的是某个特征在空间中的分布，cross-channel correlations 学习的是这些不同特征的组合方式。

**Inception的理念**  

通过一系列的 1x1 卷积来学习 cross-channel correlations，同时将输入的维度降下来；再通过常规的 3x3 和 5x5 卷积来学习 spatial correlations。 

![640](C:\myFile\notes_in_sjtu\research\paper_note\pics\deepLab\inception) 

**Inception的假设**

corss-channels correlations 和 spatial correlations 是分开学习的，而不是在某一个操作中共同学习的。 



# DeepLab V3+

论文里，作者直言不讳该框架参考了 `spatial pyramid pooling (SPP) module` 和` encoder-decoder` 两种形式的分割框架。前一种就是 `PSPNet` 那一款，后一种更像是` SegNet` 的做法。

ASPP 方法的优点是该种结构可以提取比较 dense 的特征，因为参考了不同尺度的 feature，并且 `atrous convolution` 的使用加强了提取 dense 特征的能力。但是在该种方法中由于 pooling 和有 stride 的 conv 的存在，使得分割目标的边界信息丢失严重。 

Encoder-Decoder 方法的 decoder 中就可以起到修复尖锐物体边界的作用。 

 **关于Encoder中卷积的改进**





## ref

1. https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/79710147