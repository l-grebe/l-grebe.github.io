# go常用http请求

文档链接: <https://www.cnblogs.com/zhaof/p/11346412.html>

如：
```go
//基本的GET请求
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    resp, err := http.Get("http://httpbin.org/get")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    fmt.Println(string(body))
    fmt.Println(resp.StatusCode)
    if resp.StatusCode == 200 {
        fmt.Println("ok")
    }
}
```

链接里的文档写的很详细了，而且写法也比较容易理解，这里不再做重复记录。
