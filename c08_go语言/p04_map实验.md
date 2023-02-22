# map实验

## nil map 和 empty map 区别

```go
package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

func main() {
	nilMap := new(map[string]string)
	emptyMap := make(map[string]string)

	jsonNilMap, _ := json.Marshal(nilMap)
	fmt.Println(string(jsonNilMap)) // null

	jsonEmptyMap, _ := json.Marshal(emptyMap)
	fmt.Println(string(jsonEmptyMap)) // {}

	// 判断两map是否相等
	fmt.Printf("nilMap == emptyMap: %t\n", reflect.DeepEqual(nilMap, emptyMap)) // false

	// (*nilMap)["age"] = "10" // 会报错
	emptyMap["age"] = "10" // 正常

	newMap := make(map[string][]string)
	subjects, ok := newMap["subjects"]
	fmt.Printf("subjects: %v, ok: %v\n", subjects, ok)
	fmt.Printf("len subjects: %d\n", len(subjects))
}
```

运行结果:
```text
null
{}
nilMap == emptyMap: false
subjects: [], ok: false
len subjects: 0
```