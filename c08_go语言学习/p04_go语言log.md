# go语言log

## log库基本使用
go语言的log库实现很简单，只有几十行代码，比较容易理解，直接上样例：

```go
package main

import "log"

/*
运行命令如下：
```shell
go build main.go
./main > 1.log 2>&1
```
 */

func main() {
	// 设置日志打印格式
	log.SetFlags(log.LstdFlags | log.Lmicroseconds | log.Lshortfile)
	// 会将日志输出到syscall.stderr里面。
	log.Println("123.")
	// 然后将stderr流指定到某个日志文件中，即可实现日志写入。
}
```

日志内容如下：
```
2021/05/30 08:36:59.400403 main.go:9: 123.
```

## 自定义loggers

prefix参数可以自定义日志开头

```go
package main

import (
	"log"
	"os"
)

/*
运行命令如下：
```shell
go build main.go
./main > 1.log 2>&1
```
*/

var (
	WarningLogger *log.Logger
	InfoLogger    *log.Logger
	ErrorLogger   *log.Logger
)

func init() {
	InfoLogger = log.New(os.Stderr, "INFO   : ", log.Ldate|log.Ltime|log.Lshortfile)
	WarningLogger = log.New(os.Stderr, "WARNING: ", log.Ldate|log.Ltime|log.Lshortfile)
	ErrorLogger = log.New(os.Stderr, "ERROR  : ", log.Ldate|log.Ltime|log.Lshortfile)
}

func main() {
	InfoLogger.Println("Starting the application...")
	WarningLogger.Println("There is something you should know about")
	ErrorLogger.Println("Something went wrong")
}
```
1.log文件内容为：
```
INFO   : 2021/05/30 09:07:42 main.go:29: Starting the application...
WARNING: 2021/05/30 09:07:42 main.go:30: There is something you should know about
ERROR  : 2021/05/30 09:07:42 main.go:31: Something went wrong
```

## logrus简单使用
