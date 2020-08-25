# mac-编译安装vim

```shell
git clone https://github.com/vim/vim.git

cd vim/src
make distclean
cd ..

./configure --prefix=/usr/local/vim \
--with-features=huge \
--enable-multibyte \
--enable-rubyinterp=yes \
--enable-pythoninterp=dynamic \
--enable-python3interp \
--enable-luainterp \
--enable-perlinterp=yes \
--with-python-config-dir=/usr/lib/python2.7/config \
--with-python3-config-dir=/usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/lib/python3.7/config-3.7m-darwin \
--enable-multibyte \
--enable-cscope \
--enable-fontset

sudo make install

# 添加vim软连接
ln -s /usr/local/vim/bin/vim /usr/local/bin/vim
```
