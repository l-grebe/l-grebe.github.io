# vim插件-Tagbar
Tagbar：标签侧边栏插件，该插件能够让你浏览源文件包含的标签，从而提供该源文件的结构简览。

可以将正在编辑的文件生成一个大纲, 包含类/方法/变量等, 可以选中快速跳转到目标位置, 编辑大文件特别有用.

github地址：<https://github.com/majutsushi/tagbar>



##### Tagbar的安装：

Tagbar依赖:

```shell
# ubuntu
sudo apt-get install ctags
# centos
sudo yum install ctags
# mac
brew install ctags
```

可以使用Vundle来安装，在.vimrc文件的Plugin部分加上Plugin 'tagbar',并打开vim，运行:PluginInstall命令来安装该插件



##### Tagbar配置：

在.vimrc中添加如下配置：

```shell
"------ Plugin tagbar
"autocmd vimenter * Tagbar
noremap <F10> :Tagbar<CR>  "绑定快捷键f10去打开tagbar
inoremap <F10> <esc>:Tagbar<CR>a
let g:tagbar_width=35      "tagbar宽度设置
" 设置 ctags 对哪些代码元素生成标签
let g:tagbar_type_cpp = {
    \ 'kinds' : [
        \ 'd:macros:1',
        \ 'g:enums',
        \ 't:typedefs:0:0',
        \ 'e:enumerators:0:0',
        \ 'n:namespaces',
        \ 'c:classes',
        \ 's:structs',
        \ 'u:unions',
        \ 'f:functions',
        \ 'm:members:0:0',
        \ 'v:global:0:0',
        \ 'x:external:0:0',
        \ 'l:local:0:0'
     \ ],
     \ 'sro'        : '::',
     \ 'kind2scope' : {
         \ 'g' : 'enum',
         \ 'n' : 'namespace',
         \ 'c' : 'class',
         \ 's' : 'struct',
         \ 'u' : 'union'
     \ },
     \ 'scope2kind' : {
         \ 'enum'      : 'g',
         \ 'namespace' : 'n',
         \ 'class'     : 'c',
         \ 'struct'    : 's',
         \ 'union'     : 'u'
     \ }
\ }
```



##### Tagbar快捷键使用1：

```
<F1>            显示帮助
<CR回车符>      跳到光标下tag所定义的位置，用鼠标双击此tag功能也一样
o             	在一个新打开的窗口中显示光标下tag
q             	关闭taglist窗口
u               更新taglist窗口中的tag
x               taglist窗口放大和缩小，方便查看较长的tag
s               更改排序方式，在按名字排序和按出现顺序排序间切换
```



##### Tagbar快捷键使用2：

```
+               打开一个折叠，同zo
-               将tag折叠起来，同zc
*               打开所有的折叠，同zR
=              	将所有tag折叠起来，同zM
[[            	跳到前一个文件
]]            	跳到后一个文件
<Space>       	显示光标下tag的原型定义
```
