# 树莓派编译安装vim

安装流程：

```shell
git clone https://github.com/vim/vim.git

# 提示找不到 tgetent()解决办法：安装ncurses-dev
sudo apt-get install ncurses-dev

cd vim

./configure --prefix=/usr/local/vim \
--with-features=huge \
--enable-multibyte \
--enable-rubyinterp=yes \
--enable-pythoninterp \
--enable-python3interp \
--enable-luainterp \
--enable-perlinterp=yes \
--with-python-config-dir=/usr/lib/python2.7/config-arm-linux-gnueabihf \
--with-python3-config-dir=/usr/lib/python3.7/config-3.7m-arm-linux-gnueabihf \
--enable-multibyte \
--enable-cscope \
--enable-fontset

make install

# 添加vim软连接
ln -s /usr/local/vim/bin/vim /usr/bin/vim
```
