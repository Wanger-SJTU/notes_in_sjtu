[TOC]

## linux下清除显存占用

- 结束进程如果使用 `kill PID`的命令有时候的结果是，程序挂起。而并没有终止。此时显存仍处于占用状态。

  应使用 `sudo kill PID`

  - 如果是，程序挂起，显存在占用的状态。这时候`niidia-smi`命令并不能找到其`PID`。这时候应使用 `fuser -v /dev/nvidia*` 显示而top没有显示的进程。

  - 可以根据进程查看进程相关信息占用的内存情况，(进程号可以通过ps查看)如下所示：

    ```
    ps -d 103767
    103767:   python -u pairTaskCosFeatures_GPU.py --cuda 1
    ```

     

  
