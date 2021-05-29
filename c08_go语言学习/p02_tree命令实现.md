# go语言实现的tree命令

代码如下：

```go
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)
/*
go语言实现的基本tree命令
 */

var usageDoc = `
错误的命令行参数！

    样例1： ./main .
    样例2： ./main ~/Downloads
    样例3： ./main ~/Downloads/
    样例4： ./main ~
			`

func IfElse(cmpRes bool, trueRes interface{}, falseRes interface{}) interface{} {
	if cmpRes {
		return trueRes
	}
	return falseRes
}

func genPerString(markArr []int) string {
	preString, lenArr := "", len(markArr)
	for idx, mark := range markArr {
		if idx != lenArr-1 {
			mark++
		}
		switch mark {
		case 0: // 0代表是中间的（最末级）
			preString += "├── "
		case 1: // 1代表是中间的（非最末级节点）
			preString += "│   "
		case 2: // 2代表是最后一个（最末级）
			preString += "└── "
		case 3: // 3代表是最后一个（非最末级节点）
			preString += "    "
		}
	}
	return preString
}

func printTree(path string, markArr []int) error {
	fi, err := os.Stat(path)
	if err != nil {
		return err
	}
	// 暂不显示隐藏文件
	if fi.Name()[0] == '.' && len(fi.Name()) != 1 {
		return nil
	}
	fmt.Printf("%s%s\n", genPerString(markArr), fi.Name())
	// 若是文件夹，向下执行。
	if fi.IsDir() {
		subList, _ := ioutil.ReadDir(path)
		lenSubList := len(subList)
		for idx, subFi := range subList {
			tmpVal := IfElse(idx != lenSubList-1, 0, 2).(int)
			err = printTree(strings.Join([]string{path, subFi.Name()}, "/"), append(markArr, tmpVal))
			if err != nil {
				return err
			}
		}
	}
	return nil
}

func main() {
	args := os.Args
	if len(args) == 2 {
		path := args[1]
		err := printTree(path, []int{})
		if err != nil {
			fmt.Println(err)
		}
	} else {
		fmt.Println(usageDoc)
	}
}
```
