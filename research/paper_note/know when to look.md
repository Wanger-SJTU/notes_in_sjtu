# Knowing When to Look: Adaptive Attention via A Visual Sentinel for Image Captioning

与show attention and tell 相比，创新点在于：作者认为一些非视觉词汇（the of 等）并不需要文本图像特征的支撑来获得，反而是造成干扰。

1. 提出了带有视觉标记的自适应的attention模型
2. 提出了新的spatial attention机制
3. 提出了LSTM的扩展，在hidden state以外加入了一个额外的visual sentinel vector

#### Soft attention

![](C:\myFile\notes_in_sjtu\research\paper_note\pics\caption\ada attention.png)

在show attend and tell的时候，soft attention中。如图(a)所示。

#### Adaptive Attention Model

