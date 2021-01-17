# atom配置记录

- 操作系统：macOS Catalina
- 常用atom插件：
  - `markdown-preview-plus`: (记得将markdown-preview设为禁用)
  - `vim-mode-plus`
  - `ex-mode`
  - `platformio-ide-terminal`
  - `atom-beautify`
  - `atom-ide-ui`
  - `ide-json`
  - `ide-python`
  - `pretty-json`
  - `file-icons`
  - `pigments`
  - `minimap`
- 常用atom字体：`JetBrainsMono-Regular`

### atom设置socks5代理：
```bash
~ apm -v
apm 1.19.0
npm 3.10.10
node 6.9.5 x64
atom 1.27.1
python 2.7.10
git 2.17.0

~ cat ~/.atom/.apmrc
http_proxy=socks5:127.0.0.1:1080
https_proxy=socks5:127.0.0.1:1080
strict-ssl=false
```

### 安装platformio-ide-terminal插件后PS1乱码解决：
platformio-ide-terminal插件使用`JetBrainsMono-Medium`字体即可，该字体可直接去<https://www.jetbrains.com/zh-cn/lp/mono/>下载。

已弃用解决方法：
> zsh部分主题需要Powerline Fonts，但在atom的terminal下目前没有找到如何指定terminal字体，
  发现 platformio Ide Terminal 下有Shell Environment Variables配置项,于是在该栏添加
  了 `FROM_APP=atom` ,然后在 `.zshrc` 中写个if else,换另一个theme就好了，代码如下：
  ```bash
  if [ "$FROM_APP" = "atom" ]; then
  ZSH_THEME="michelebologna"
  echo "docsify serve ."
  else
  ZSH_THEME="agnoster"
  fi
  ```

atom不显示红色的下划线：
> 禁用spell-check这一package即可.

atom markdown-preview-plus 快速显示markdown预览快捷键：`ctrl+shift+m`
