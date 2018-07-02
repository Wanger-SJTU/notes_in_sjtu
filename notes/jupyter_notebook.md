# notes about jupyter



## **Jupyter Notebooks 的神奇功能** 

### magic command

> %lsmagic

你会看到列出了很多选择，你甚至可能能认出其中一些！`%clear`、`%autosave`、`%debug` 和 `%mkdir` 等功能你以前肯定见过。

>```
>Available line magics:
>%alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %cls  %colors  %config  %connect_info  %copy  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %ren  %rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
>
>Available cell magics:
>%%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
>
>Automagic is ON, % prefix IS NOT needed for line magics.
>```

现在，神奇的命令可以以两种方式运行： 

- 逐行方式
- 逐单元方式

顾名思义，逐行方式是执行单行的命令，而逐单元方式则是执行不止一行的命令，而是执行整个单元中的整个代码块。

在逐行方式中，所有给定的命令必须以 % 字符开头；而在逐单元方式中，所有的命令必须以 %% 开头。我们看看下列示例以便更好地理解：

逐行方式：

```
%time a = range(10)
```

逐单元方式：

```
%%timeit a = range (10)
min(a)
```

 ### Jupyte Lab





 