# vim配色方案

vim配色下载地址：<https://vimcolors.com>

##### 常用配色方案下载：

molokai：

```shell
cd /tmp && rm -vrf molokai && git clone https://github.com/vim-scripts/molokai.git
cp -vf ./molokai/colors/molokai.vim ~/.vim/colors/
rm -vrf molokai
```

Solarized：

```shell
cd /tmp && rm -vrf vim-colors-solarized && git clone git://github.com/altercation/vim-colors-solarized.git
cp -vf ./vim-colors-solarized/colors/solarized.vim ~/.vim/colors/
rm -vrf vim-colors-solarized
```

phd:

```shell
cd /tmp && rm -vrf phd && git clone https://github.com/vim-scripts/phd
cp -vf ./phd/colors/phd.vim ~/.vim/colors/
rm -vrf phd
```



##### 配色方案使用：

在.vimrc文件中添加如下配置即可

```shell
set background=dark
colors solarized
```

**vim 内置定义了一些颜色以方便使用，通常包括：**

```shell
Red     LightRed        DarkRed
Green   LightGreen      DarkGreen       SeaGreen
Blue    LightBlue       DarkBlue        SlateBlue
Cyan    LightCyan       DarkCyan
Magenta LightMagenta    DarkMagenta
Yellow  LightYellow     Brown           DarkYellow
Gray    LightGray       DarkGray
Black   White
Orange  Purple          Violet
```
