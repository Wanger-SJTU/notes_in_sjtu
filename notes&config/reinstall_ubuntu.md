1. 重装系统过程

    重装过程选择，略过 。以下为注意事项。

    1. 更改ubuntu的源

        可以选择清华、交大、中科大的

    2. ​

2. 安装显卡驱动 

    **注：** 这种安装方式在执行`sudo apt-get upgrade`命令以后，如果内核升级（linux下比较频繁）会使得驱动重新安装编译。慎重使用`sudo apt-get upgrade`命令

    1. 下载安装
        1. 禁用原来的驱动  

            >sudo apt-get remove nvidia* && sudo apt-get autoremove
            >sudo apt-get install dkms build-essential linux-headers-generic
            >sudo vim /etc/modprobe.d/blacklist.conf

        2. 添加下面内容  
          
            > blacklist nouveau     
              blacklist lbm-nouveau  
              options nouveau modeset=0  
              alias nouveau off  
              alias lbm-nouveau off
            
        3. >sudo update-initramfs -u

        4. 检查是否卸载干净

            > lsmod | grep nouveau  
              lsmod | grep nvidia*
            
        5. 重启

            > reboot

        6. `ctrl + alt + F1` 进入文本模式
        7. 关闭桌面

            > sudo service lightdm stop
            
        8. 安装 Nvidia Driver(需要提前下载好)

            > sudo chmod 755 NVIDIA-Linux-x86_64-367.27.run  
             sudo ./NVIDIA-Linux-x86_64-367.27.run

        9. 打开桌面

            > sudo service lightdm start

    2. ppa模式
        - a. to g. 与上面相同  

        8. 添加ppa源

            > sudo add-apt-repository ppa:graphics-drivers/ppa  
                sudo apt-get update
            
        9. 选择安装合适的driver

            > sudo apt-get install nvidia-
            
            按 `TAB` 键选择

3. 安装CUDA
    1. [这里](https://developer.nvidia.com/cuda-downloads)选择cuda 版本(此处为9.1)
        从官网下载 安装即可，注意不安装驱动（上面已经安装好了）
    2. cuda 安装完成之后，在`~/.bashrc` 中添加以下环境变量即可。

        >   export CUDA_HOME=/usr/local/cuda-9.1  
            export PATH=/usr/local/cuda-9.1/bin${PATH:+:${PATH}}  
            export LD_LIBRARY_PATH=/usr/local/cuda-9.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}  

    3. `source ~/.bashrc` 生效
    4. `nvcc -V`检查安装情况
       -  编译`NVIDIA CUDA SAMPLES` examples失败 提示 `/usr/bin/ld:can not find -lgult`时 安装 `sudo apt-get install freeglut3 freeglut3-dev`

    5. 编译 `nvidia cuda samples`

4. 安装 `anaconda`

    **注：** 强烈建议在不同的项目中建立不同的虚拟环境，避免不同的包污染。

    > conda create -n python=*.*

    ​

    1. 添加环境变量，具体参照安装完后的提示。

    2. 添加 anaconda的源地址为[清华](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)的。

    3. `jupter notebook`  
        - 为了可以在`jupyter notebook` 中可以识别不同的虚拟环境, 需要安装包  

            > conda install nb_conda  

        - `Permission Denied(13)  `  

            >sudo chown -R user anaconda3

        - 为了不同的环境均可以在`jupyter notebook`中识别，需要在每个环境安装包
            > conda install ipykernel
            
        - ​

    4. ​

5. 安装 `opencv`   

    1. 如果只在`python`中使用`opencv`可以使用`conda install opencv`安装`python`的包。

    2. 编译opencv

       注意opencv的版本要与cuda版本对应。

    3. ​

    #### optional

6. 安装 `ss-qt5`

    > ​

7. 安装 `sublime`

    参照官网操作即好。

8. 安装 `chrome`

9. 安装 `ROS` 
