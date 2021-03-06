# vim插件-NERDTree

NERDTree的作用就是列出当前路径的目录树，可以方便的浏览项目的总体的目录结构和创建删除重命名文件或文件名。

github地址：https://github.com/scrooloose/nerdtree



##### NERDTree在.vimrc中添加的配置:

```shell
"------ Plugin NERDTree
let NERDTreeWinSize=30 "设置目录展示的宽度

"列出当前目录文件
map <F9> :NERDTreeToggle<CR>  "使用f9快捷键调出和隐藏目录树
imap <F9> <ESC> :NERDTreeToggle<CR>

"当打开vim且没有文件时自动打开NERDTree
autocmd vimenter * if !argc() | NERDTree | endif     	
" 只剩 NERDTree时自动关闭
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
" autocmd bufenter * if (winnr("$") == 1) | q | endif
```

##### NERDTree常用操作1：

```shell
# 打开文件和目录树：
# 原窗口：
o       在已有窗口中打开文件、目录或书签，并跳到该窗口
go      在已有窗口 中打开文件、目录或书签，但不跳到该窗口
# 新窗口-横向：
i       split 一个新窗口打开选中文件，并跳到该窗口
gi      split 一个新窗口打开选中文件，但不跳到该窗口
# 新窗口-纵向：
s       vsplit 一个新窗口打开选中文件，并跳到该窗口
gs      vsplit 一个新 窗口打开选中文件，但不跳到该窗口
# 新Tab：
t       在新 Tab 中打开选中文件/书签，并跳到新 Tab
T       在新 Tab 中打开选中文件/书签，但不跳到新 Tab
```

##### NERDTree常用操作2：

```shell
C       将选中目录或选中文件的父目录设为根结点
u       将当前根结点的父目录设为根目录，并变成合拢原根结点
U       将当前根结点的父目录设为根目录，但保持展开原根结点

r       递归刷新选中目录

!       执行当前文件
O       递归打开选中 结点下的所有目录
x       合拢选中结点的父目录
X       递归 合拢选中结点下的所有目录
e       Edit the current dif
双击    相当于 NERDTree-o
中键    对文件相当于 NERDTree-i，对目录相当于 NERDTree-e
D       删除当前书签
P       跳到根结点
p       跳到父结点
K       跳到当前目录下同级的第一个结点
J       跳到当前目录下同级的最后一个结点
k       跳到当前目录下同级的前一个结点
j       跳到当前目录下同级的后一个结点

R       递归刷新根结点
m       显示文件系统菜单 #！！！然后根据提示进行文件的操作如新建，重命名等
cd      将 CWD 设为选中目录
I       切换是否显示隐藏文件
f       切换是否使用文件过滤器
F       切换是否显示文件
B       切换是否显示书签
q       关闭 NerdTree 窗口
?       切换是否显示 Quick Help
```
