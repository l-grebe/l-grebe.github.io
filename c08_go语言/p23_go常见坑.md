# go常见坑

### any 与 nil 的比较

- doc: <https://cloud.tencent.com/developer/article/1911289>

实验代码：

```go
package main

import "fmt"

func IsNil(i interface{}) {
	if i == nil {
		fmt.Println("i is nil")
		return
	}
	fmt.Println("i isn't nil")
}

func main() {
	var sl []string
	if sl == nil {
		fmt.Println("sl is nil")
	}
	IsNil(sl)
}
```

运行结果：

```text
sl is nil
i isn't nil
```

要想理解这个问题，首先需要理解 interface{} 变量的本质。


