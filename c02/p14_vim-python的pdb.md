# vim-python的pdb

### 1. python-mode添加断点：

运行python code: `<leader>r`

增加/移除 python 断点: `<leader>b`

代码内添加断点：

```python
import pdb
pdb.set_trace()
```



##### 2.pdb使用

pdb是python自带的debug工具。

pdb常用调试命令（进入pdb后，输入help可以查看）：

| 命令                | 解释                       |
| ------------------- | -------------------------- |
| break 或 b 设置断点 | 设置断点                   |
| continue 或 c       | 继续执行程序               |
| list 或 l           | 查看当前行的代码段         |
| step 或 s           | 进入函数                   |
| return 或 r         | 执行代码直到从当前函数返回 |
| exit 或 q           | 中止并退出                 |
| next 或 n           | 执行下一行                 |
| pp                  | 打印变量的值               |
| help                | 帮助                       |
