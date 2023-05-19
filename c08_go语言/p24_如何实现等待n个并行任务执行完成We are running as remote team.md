# 如何实现等待n个并行任务执行完成

- 思考：处理任务时，有N个子任务可以并发执行，这种代码要怎么编写？
- 例子：在执行任务A时，下面有a1、a2、a3、......、an个子任务，如何编写代码能最快的完成该任务A。


### 代码实现:
```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

type bsonM map[string]interface{}

func TimeCost(hint string, start time.Time) {
	tc := time.Since(start)
	fmt.Printf("%s time cost = %v\n", hint, tc)
}

func MinInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type itemAnaResult struct {
	Id     string
	Result bsonM
}

type ItemAna struct {
	Id      string
	Subject string
	PaperId string
}

// Analysis 数据分析具体执行逻辑
func (p *ItemAna) Analysis() bsonM {
	defer TimeCost(fmt.Sprintf("deal the item %s analysis", p.Id), time.Now())
	randomNum := rand.Float64() * 5
	res := make(bsonM)
	res["id"] = p.Id
	res["subject"] = p.Subject
	res["paper_id"] = p.PaperId
	time.Sleep(time.Duration(randomNum) * time.Second)
	return res
}

func (p *ItemAna) AnalysisByGoroutine(ch chan<- *itemAnaResult) {
	ch <- &itemAnaResult{
		Id:     p.Id,
		Result: p.Analysis(),
	}
}

func NewItemAna(id string, subject string, paperId string) *ItemAna {
	return &ItemAna{Id: id, Subject: subject, PaperId: paperId}
}

type ItemAnaList []*ItemAna

// Analysis 并发的处理每个小问的分析
func (p *ItemAnaList) Analysis() bsonM {
	defer TimeCost("deal the item list analysis", time.Now())
	ch := make(chan *itemAnaResult)
	res := make(bsonM)
	for _, item := range *p {
		go item.AnalysisByGoroutine(ch)
	}
	for _, _ = range *p {
		one := <-ch
		res[one.Id] = one.Result
	}
	return res
}
func (p *ItemAnaList) Len() int {
	return len(*p)
}

// AnalysisByCustomGoroutineNum 并发的处理每个小问的分析，但是每次只并发固定的任务数量
func (p *ItemAnaList) AnalysisByCustomGoroutineNum(num int) bsonM {
	if num <= 0 {
		panic("Invalid number")
	}
	defer TimeCost("deal the item list analysis", time.Now())
	res := make(bsonM)
	for i := 0; i < p.Len(); i += num {
		partItems := (*p)[i:MinInt(i+num, p.Len())]
		partRes := partItems.Analysis()
		for k, v := range partRes {
			res[k] = v
		}
		fmt.Println()
	}
	return res
}

type PaperAna struct {
	Id      string
	Subject string
	ItemsId []string
}

func (p *PaperAna) Analysis() bsonM {
	defer TimeCost("deal the paper analysis", time.Now())
	res := make(bsonM)
	res["subject"] = p.Subject
	res["id"] = p.Id
	return res
}

func NewPaperAna(subject string, id string, itemsId []string) *PaperAna {
	return &PaperAna{
		Subject: subject,
		Id:      id,
		ItemsId: itemsId,
	}
}

func analysis() bsonM {
	res := make(bsonM)
	subject := "chinese"
	paperId := "60e4e722f3182d405d6eb505"
	itemsId := []string{"0_1", "0_2", "0_3", "1_1", "2_1", "3_1", "4_1", "5_1", "6_1", "7_1"}
	// analysis paper
	paperAna := NewPaperAna(subject, paperId, itemsId)
	res["paper"] = paperAna.Analysis()
	// analysis items
	itemsAna := make(ItemAnaList, 0)
	for _, itemId := range itemsId {
		itemsAna = append(itemsAna, NewItemAna(itemId, subject, paperId))
	}
	// res["items"] = itemsAna.Analysis()
	res["items"] = itemsAna.AnalysisByCustomGoroutineNum(3)
	return res
}

func main() {
	rand.Seed(time.Now().UnixNano())
	analysis()
}

```