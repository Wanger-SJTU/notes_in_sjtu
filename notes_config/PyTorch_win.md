# PyTorch Windows版安装教程



## 安装准备
1. **Python**
    ```bash
    pip install numpy pyyaml
    ```
2. **Cuda**和**CuDNN**
    请安装Cuda 8.0及以上版本
3. **Microsoft Visual Studio**
    |Cuda 版本|支持的VS版本|
    |---------|-----------|
    |   8.0   | 2013/2015 |
    | 9.0/9.1 | 2015/2017*|
    **注：** Cuda对VS2017支持的C/C++编译器仅限于19.11版本，不支持19.12和19.13。如需使用VS2017，请按以下步骤将默认C/C++编译器切换至19.11版本。
    **检查方法：** 开始菜单->Visual Studio 2017->适用于 VS 2017 的 x64 本机工具命令提示，输入`cl.exe`，即可看到当前使用的C/C++编译器版本
    **切换方法：**

    1. `开始菜单`->`Visual Studio Installer`->`修改`->`单个组件`->勾选`VC++ 2017 版本 15.4 v14.11 工具集`->修改

    ​    2. 打开目录`C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\VC\Tools\MSVC`,可以看到有几个以版本号命名的文件夹，复制以14.11开头的文件夹的名字，如`14.11.25503`
        3. 打开目录`C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\VC\Auxiliary\Build`，修改`Microsoft.VCRedistVersion.default.txt`、`Microsoft.VCToolsVersion.default.props`和`Microsoft.VCToolsVersion.default.txt`，将原来的编译器版本号全部替换成步骤2中以14.11开头的版本号
        4. 打开`适用于 VS 2017 的 x64 本机工具命令提示`，检查编译器是否切换为19.11版本
4. **CMake**
    下载地址：`https://cmake.org/download/`
    请将`cmake.exe`所在目录加入`PATH`环境变量
5. **Git**
    下载地址：<https://git-scm.com/>
    请将`git.exe`所在目录加入`PATH`环境变量
6. **JOM**
    JOM是一个NMakefile的并行化编译工具。NMake默认只能单线程编译，编译速度很慢，使用JOM可以大大缩短编译时间。
    下载地址：<http://download.qt.io/official_releases/jom/>
    请将`jom.exe`放置到`cmake.exe`所在目录
7. Intel MKL（非必需）
    MKL(Math Kernel Library)是Intel开发的一个数学库，可以大大加快Intel处理器上矩阵运算速度
    下载地址：<https://software.intel.com/en-us/mkl>

## 安装过程
1. clone 官方 repo，并复制common_with_cwrap.py
    ```bash
    git clone --recursive https://github.com/pytorch/pytorch
    cd pytorch
    xcopy /Y aten\src\ATen\common_with_cwrap.py tools\shared\cwrap_common.py
    ```
    **注：**
    - 必须使用--recursive的方式下载，不可以直接从github上下载zip压缩包，因为github上下载的源代码不包含众多submodules
    - 请自备梯子，否则下载过程会很痛苦
    - 不要忘记将复制common_with_cwrap，否则编译会出错
    - 可能存在一个快捷方式的cwrap_common.py文件。需要先删除，不然有共享冲突

2. 编辑`pytorch/tools/build_pytorch_libs.bat`
    - 在第46行 修改CMake Generator设置
        ```
        IF "%CMAKE_GENERATOR%"=="" (
        set CMAKE_GENERATOR_COMMAND=
        set MAKE_COMMAND=msbuild INSTALL.vcxproj /p:Configuration=Release
        ) ELSE (
        set CMAKE_GENERATOR_COMMAND=-G "%CMAKE_GENERATOR%"
        IF "%CMAKE_GENERATOR%"=="Ninja" (
            IF "%CC%"== "" set CC=cl.exe
            IF "%CXX%"== "" set CXX=cl.exe
            set MAKE_COMMAND=cmake --build . --target install --config %BUILD_TYPE% -- -j%MAX_JOBS%
        ) ELSE (
            set MAKE_COMMAND=msbuild INSTALL.vcxproj /p:Configuration=%BUILD_TYPE%
        )
        )
        ```
        修改为
        ```
        set CMAKE_GENERATOR_COMMAND=-G "NMake Makefiles JOM"
        set MAKE_COMMAND=jom install
        ```
    * 修改CMake标志设置
        如未使用MKL，请跳过此步骤；如使用MKL，请在`:build`和`:build_aten`的cmake命令后补充如下flag：
        ```
        -DINTEL_MKL_DIR="C:/Program Files (x86)/IntelSWTools/compilers_and_libraries/windows/mkl" ^
        -DMKL_LIBRARIES_pthread_LIBRARY="D:/Libraries/pthread/lib/pthreadVC2.lib" ^
        -DMKL_LIBRARIES_libiomp5md_LIBRARY="C:/Program Files (x86)/IntelSWTools/compilers_and_libraries/windows/compiler/lib/intel64/libiomp5md.lib"
        ```
        **注：** 命令换行时，不要忘记用`^`符号转义

3. 编译安装
        打开`适用于 VS 2017 的 x64 本机工具命令提示`，`cd`至PyTorch源文件目录下，执行以下命令

   ```
    python setup.py install
   ```

   ​     等待数小时，即可完成安装！

   by王昊天