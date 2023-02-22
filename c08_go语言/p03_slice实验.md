# slice实验

### nil slice 和 empty slice 的区别

示例代码：

```go
package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

func main() {
	var nilSlice []string
	jsonNilSlice, _ := json.Marshal(nilSlice)
	fmt.Println(string(jsonNilSlice)) // null
	fmt.Println(len(nilSlice))

	emptySlice := make([]string, 0)
	jsonEmptySlice, _ := json.Marshal(emptySlice)
	fmt.Println(string(jsonEmptySlice)) // []
	fmt.Println(len(emptySlice))

	// 判断两slice是否相等
	fmt.Printf("nilSlice == emptySlice: %t\n", reflect.DeepEqual(nilSlice, emptySlice)) // false
}

```

运行结果:

```text
null
0
[]
0
nilSlice == emptySlice: false

```

### 切片实验

代码如下：

```go
package main

import "fmt"

func main() {
	var a []int
	a = append(a, 1, 2)
	fmt.Printf("a: %p %d %v\n", a, len(a), a)
	b := append(a, 3, 4)
	fmt.Printf("b: %p %d %v\n", b, len(b), b)
	fmt.Println()

	a[0] = 10
	fmt.Printf("a: %p %d %v\n", a, len(a), a)
	fmt.Printf("b: %p %d %v\n", b, len(b), b)
	fmt.Println()

	c := b[1:3]
	b[2] = 30
	fmt.Printf("b: %p %d %v\n", b, len(b), b)
	fmt.Printf("c: %p %d %v\n", c, len(c), c)
	fmt.Println()

	d := make([]int, 2)
	copy(d, b[1:3])
	b[2] = 300
	fmt.Printf("b: %p %d %v\n", b, len(b), b)
	fmt.Printf("d: %p %d %v\n", d, len(d), d)
	fmt.Println()

}
```

结果如下：

```
a: 0xc0000ae010 2 [1 2]
b: 0xc0000b0040 4 [1 2 3 4]

a: 0xc0000ae010 2 [10 2]
b: 0xc0000b0040 4 [1 2 3 4]

b: 0xc0000b0040 4 [1 2 30 4]
c: 0xc0000b0048 2 [2 30]

b: 0xc0000b0040 4 [1 2 300 4]
d: 0xc0000ae0c0 2 [2 30]

```

奇怪的append函数！

