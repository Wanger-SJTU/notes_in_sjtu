

[TOC]

# RuntimeError: already counted a million dimensions in a given sequence.

完整错误信息

```
Train:   0%|                                             | 0/10 [00:00<?, ?it/s]
Train epoch=0:   0%|                                     | 0/26 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "train.py", line 123, in <module>
    main()
  File "train.py", line 118, in main
    trainer.train()
  File "C:\myFile\code\image_scene_classification\CH\model\trainer.py", line 306, in train
    self.train_epoch()
  File "C:\myFile\code\image_scene_classification\CH\model\trainer.py", line 213, in train_epoch
    desc='Train epoch=%d' % self.epoch, ncols=80, leave=False):
  File "C:\Users\chmtt\Anaconda3\envs\SCENE\lib\site-packages\tqdm\_tqdm.py", line 941, in __iter__
    for obj in iterable:
  File "C:\Users\chmtt\Anaconda3\envs\SCENE\lib\site-packages\torch\utils\data\dataloader.py", line 259, in __next__
    batch = self.collate_fn([self.dataset[i] for i in indices])
  File "C:\Users\chmtt\Anaconda3\envs\SCENE\lib\site-packages\torch\utils\data\dataloader.py", line 259, in <listcomp>
    batch = self.collate_fn([self.dataset[i] for i in indices])
  File "C:\myFile\code\image_scene_classification\CH\data\dataset.py", line 73, in __getitem__
    return self.transform(img), torch.FloatTensor(lbl)
RuntimeError: already counted a million dimensions in a given sequence. Most likely your items are also sequences and there's no way to infer how many dimension should the tensor have
```

**solution**

输入标签必须为数字

# cannot unsqueeze empty tensor at /opt/conda/conda-bld/pytorch_1512378360668/work/torch/lib/TH/generic/THTensor.c:601

以下报错信息来自网上，与遇到的问题相同

```
Traceback (most recent call last):
  File "UCF101_pytorch_fyq.py", line 182, in <module>
    for i_batch,sample_batched in enumerate(dataloader):
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 210, in __next__
    return self._process_next_batch(batch)
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 230, in _process_next_batch
    raise batch.exc_type(batch.exc_msg)
RuntimeError: Traceback (most recent call last):
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 42, in _worker_loop
    samples = collate_fn([dataset[i] for i in batch_indices])
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 116, in default_collate
    return {key: default_collate([d[key] for d in batch]) for key in batch[0]}
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 116, in <dictcomp>
    return {key: default_collate([d[key] for d in batch]) for key in batch[0]}
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/utils/data/dataloader.py", line 96, in default_collate
    return torch.stack(batch, 0, out=out)
  File "/home/hl/anaconda2/lib/python2.7/site-packages/torch/functional.py", line 62, in stack
    inputs = [t.unsqueeze(dim) for t in sequence]
RuntimeError: invalid argument 2: cannot unsqueeze empty tensor at /opt/conda/conda-bld/pytorch_1512378360668/work/torch/lib/TH/generic/THTensor.c:601
```

- 分析

报错信息来自于DataLoader，对于确实是由于label是标量引起的，最后做了改动

- 解决方法

  直接返回数字，即可