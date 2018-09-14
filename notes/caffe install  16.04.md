1. 安装依赖

   > sudo apt-get install python-pip
   >
   > sudo pip install easydict protobuf pydot
   >
   > sudo apt-get install graphviz libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler libopenblas-dev liblapack-dev libatlas-base-dev libgflags-dev libgoogle-glog-dev liblmdb-dev python-tk python-numpy python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags
   >
   > sudo apt-get install --no-install-recommends libboost-all-dev

2. nvidia-smi 驱动以及CUDA cudnn

3. 配置caffe

   - 下载caffe

   - 配置caffe文件

     > cd  caffe（具体路径自己改）
     >
     > sudo cp Makefile.config.example Makefile.config
     >
     > sudo gedit Makefile.config
     >
     > USE_CUDNN := 1#去掉这个注释，因为要使用cudnn（但是假如显卡太低级，兼容性不够，就用不了cudnn）
     >
     > \# CPU_ONLY := 1#加上这个注释（因为要使用cuda，所以就不用改）
     >
     > WITH_PYTHON_LAYER := 1 #去掉这个注释，因为以后经常会用到caffe 的 Python layer
     >
     > 然后根据自己的cuda根据该文档提示删去或者注释掉相应的版本的，例如
     >
     > CUDA_ARCH := #-gencode arch=compute_20,code=sm_20 \
     >
     > \#-gencode arch=compute_20,code=sm_21 \（要根据自己实际才cuda版本注释，文件本身有提示）
     >
     > 将
     >
     > INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
     >
     > LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib
     >
     > 修改为：
     >
     > INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/include/hdf5/serial
     >
     > LIBRARY_DIRS := $(PYTHON_LIB) /usr/lib/x86_64-linux-gnu/hdf5/serial（一般是这两条，具体路径可以自己看机器的hdf5文件夹路径）
     >
     > 保存退出。

   - 编译caffe

     > sudo make all -j16 （在make pycaffe -j16前的话会有很多编译错误，以后的bug）
     >
     > sudo make runtest -j16（测试）
     >
     > sudo make pycaffe -j16（警告不用在意，在make all -j16前会好一点，很少error）
     >
     > sudo make pytest -j16
     >
     > 若报错，则需要
     >
     > sudo make clean
     >
     > 然后修改错误后，重新编译编译caffe

4. 错误处理

   - **m//home/yali/anaconda2/lib/libpng16.so.16：对‘inflateValidate@ZLIB_1.2.9’未定义的引用**   

     正确解决方法：  

     > 在 Makefile.config 中，加入下一句  LINKFLAGS := -Wl,-rpath,$(HOME)/anaconda3/lib

5. 