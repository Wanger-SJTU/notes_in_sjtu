# 禁用 `rm`

[refer](https://blog.csdn.net/gatieme/article/details/49101227)

## 回收站命令行工具trash-cli

```bash
sudo apt-get install trash-cli
```

命令概览：

| Tables        | Are                    | Cool |
| ------------- | ---------------------- | ---- |
| trash-put     | 将文件或目录移入回收站 |      |
| trash-empty   | 清空回收站             |      |
| trash-list    | 列出回收站中的文件     |      |
| restore-trash | 还原回收站中的文件     |      |
| trash-rm      | 删除回收站中的单个文件 |      |

## rm和trash

 如果只是想本用户使用，就修改`~/.profile`或者`~/.bashrc  `

如果想要全局使用，就使用`/etc/profile`或者`/etc/bashrc`中 

在文件中加入

```
alias rm="trash"1
```

或者

```
alias rm=”trush-put”
```