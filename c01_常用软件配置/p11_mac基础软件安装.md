# mac基础软件安装

### 基础软件
```shell
# 安装git
# terminal 输入git后会有安装路径。

# 安装iTerm2: `https://iterm2.com/`

# 安装oh my zsh: `https://ohmyz.sh/`
# oh my zsh 主题推荐: `https://github.com/ohmyzsh/ohmyzsh/wiki/Themes`

# 安装Homebrew: `https://brew.sh/`

# 安装tree, htop: 
brew install tree top 

```

### zsh里添加http_proxy:

`~/.zshrc`文件里添加如下配置:
```shell
# 打开代理
function proxy_on() {
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
    export http_proxy="http://127.0.0.1:1081"
    export https_proxy=$http_proxy
    echo -e "已开启代理"
}
# 关闭代理
function proxy_off(){
    unset http_proxy
    unset https_proxy
    echo -e "已关闭代理"
}
```