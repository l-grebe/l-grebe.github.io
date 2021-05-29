# go安装与包管理

- OS: MacOS
- go version: 1.16.4
- 安装包下载网址：<https://golang.org/doc/install?download=go1.16.4.darwin-amd64.pkg>

## 安装go并做相关配置

直接下载pkg文件，点击安装即可。

查看go可执行文件安装位置：
```shell
~ which go
/usr/local/go/bin/go
```


`.zshrc`文件中配置GOPATH：
```shell
# GOPATH
export GOPATH="/Users/husy/Documents/gopath"
```

设置GOPROXY：
```shell
go env -w GOPROXY=https://goproxy.io,direct
```

开启新terminal窗口后，运行`go env`可查看设置情况：

## 安装第3方包

创建工程目录：
```shell
mkdir awesomeProject
cd awesomeProject
```

main.go内容如下：
```go
package main

import (
	"fmt"
	"github.com/spf13/pflag"
)

func main() {

	fmt.Println("hello, world")

	flags := pflag.NewFlagSet("kubectl-convert", pflag.ExitOnError)
	pflag.CommandLine = flags
	fmt.Println(flags)
}
```

运行如下命令安装包，更多说明可通过`go mod help`命令查看：
```shell
go mod init awesomeProject # 在当前目录中初始化新模块
go mod tidy # 添加缺少的内容并删除未使用的模块
go mod vendor # 生成vendor文件夹，制作依赖关系的供应副本
```

运行完成后，当前目录展示如下：
```shell
.
├── go.mod
├── go.sum
├── main.go
└── vendor
    ├── github.com
    │   └── spf13
    │       └── pflag
    │           ├── LICENSE
    │           ├── README.md
    │           ├── bool.go
    │           ├── bool_slice.go
    │           ├── bytes.go
    │           ├── count.go
    │           ├── duration.go
    │           ├── duration_slice.go
    │           ├── flag.go
    │           ├── float32.go
    │           ├── float32_slice.go
    │           ├── float64.go
    │           ├── float64_slice.go
    │           ├── go.mod
    │           ├── go.sum
    │           ├── golangflag.go
    │           ├── int.go
    │           ├── int16.go
    │           ├── int32.go
    │           ├── int32_slice.go
    │           ├── int64.go
    │           ├── int64_slice.go
    │           ├── int8.go
    │           ├── int_slice.go
    │           ├── ip.go
    │           ├── ip_slice.go
    │           ├── ipmask.go
    │           ├── ipnet.go
    │           ├── string.go
    │           ├── string_array.go
    │           ├── string_slice.go
    │           ├── string_to_int.go
    │           ├── string_to_int64.go
    │           ├── string_to_string.go
    │           ├── uint.go
    │           ├── uint16.go
    │           ├── uint32.go
    │           ├── uint64.go
    │           ├── uint8.go
    │           └── uint_slice.go
    └── modules.txt
```
依赖的包已经安装，直接运行main.go:
```shell
~ go run main.go
hello, world
&{<nil> true {false} kubectl-convert false map[] [] [] map[] [] [] map[] [] -1 1 <nil> true <nil> []}
```
