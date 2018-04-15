## nll_loss 异常报错



bug描述

> /pytorch/torch/lib/THCUNN/ClassNLLCriterion.cu:101: void cunn_ClassNLLCriterion_updateOutput_kernel(Dtype *, Dtype *, Dtype *, long *, Dtype *, int, int, int, int, long) [with Dtype = float, Acctype = float]: block: [0,0,0], thread: [23,0,0] Assertion `t >= 0 && t < n_classes` failed.
> /pytorch/torch/lib/THCUNN/ClassNLLCriterion.cu:101: void cunn_ClassNLLCriterion_updateOutput_kernel(Dtype *, Dtype *, Dtype *, long *, Dtype *, int, int, int, int, long) [with Dtype = float, Acctype = float]: block: [0,0,0], thread: [24,0,0] Assertion `t >= 0 && t < n_classes` failed.
> THCudaCheck FAIL file=/pytorch/torch/lib/THC/generic/THCTensorCopy.c line=70 error=59 : device-side assert triggered

ClassNLLCriterion.cu相关代码

```cpp
template <typename Dtype>
__global__ void cunn_ClassNLLCriterion_updateOutput_kernel1(Dtype *output,
                                                           Dtype *total_weight,
                                                           Dtype *input,
                                                           THCIndex_t  *target,
                                                           Dtype *weights,
                                                           int size_average,
                                                           int n_classes,
                                                           int64_t ignore_index) {
  assert(threadIdx.x == 0 && threadIdx.y == 0 && threadIdx.z == 0);

  // TODO: T4951791 Reuse code between updateOutput_kernel1 and
  // updateOutput_kernel.

  int t = (int) *target - TH_INDEX_BASE;
  if (t != (int) ignore_index) {
    assert(t >= 0 && t < n_classes);
    Dtype cur_weight = weights ? weights[t] : ScalarConvert<int, Dtype>::to(1);
    *output = -cur_weight * input[t];
    *total_weight = cur_weight;
    if (size_average && *total_weight > 0) {
      *output /= *total_weight;
    }
  }
}
```

注意对`target`进行了参数检查

```cpp
 assert(t >= 0 && t < n_classes);
```

回到`torch.nn.functional.nll_loss`函数说明

>- **input** –$ (N,C)$ where $C = $ number of classes or $(N,C,H,W)$ in case of $2D$ Loss, or $(N,C,d_1,d_2,...,d_K)$ where$K>1$ in the case of $K$-dimensional loss.
>- **target** – $(N)$where each value is $0 <= targets[i] <= C-1$, or $(N,C,d_1,d_2,...,d_K)$where $K>=1 $for $K$-dimensional loss.
>- **weight** ([*Tensor*](http://pytorch.org/docs/stable/tensors.html#torch.Tensor)*,* *optional*) – a manual rescaling weight given to each class. If given, has to be a Tensor of size C
>- **size_average** ([*bool*](https://docs.python.org/2/library/functions.html#bool)*,* *optional*) – By default, the losses are averaged over observations for each minibatch. If size_average is False, the losses are summed for each minibatch. Default: `True`
>- **ignore_index** ([*int*](https://docs.python.org/2/library/functions.html#int)*,* *optional*) – Specifies a target value that is ignored and does not contribute to the input gradient. When size_average is True, the loss is averaged over non-ignored targets. Default: -100

这里`target`参数得`max_value` 为`input`通道数（即类别）

原来得代码中，对类别数确定失误。