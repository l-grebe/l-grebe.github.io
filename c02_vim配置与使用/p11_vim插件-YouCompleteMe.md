# vim插件-YouCompleteMe
YouCompleteMe是一款vim下的代码补全插件

github地址：<https://github.com/Valloric/YouCompleteMe>

youcompleteMe官方文档：<https://github.com/Valloric/YouCompleteMe/blob/master/doc/youcompleteme.txt>



##### ubuntu安装：

1. 安装开发工具和cmake：

   ```shell
   sudo apt-get install build-essential cmake
   ```

2. 确认Python headers已经安装：

   ```shell
   sudo apt-get install python-dev python3-dev
   ```

3. YouCompleteMe下载

   在.vimrc的Bundle插件中加入如下行：

   ```
   Bundle 'Valloric/YouCompleteMe'
   ```

   打开vim并输入`:BundleInstall`，来完成YouCompleteMe的下载

4. 编译安装YouCompleteMe

   ```shell
   cd ~/.vim/bundle/YouCompleteMe
   ./install.sh
   # ./install.sh --clang-completer 需要写c代码时再加
   ```



##### YouCompleteMe快捷键：

当出现提示后，按tab(或者`ctrl+n`）键可以向下选择。
