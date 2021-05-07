# fastapi async写法与同步性能比较

参考文档：<https://blog.csdn.net/yyw794/article/details/108859240>

### 一，我们先用fastapi实现三种处理响应的接口，其延时均为1s，代码如下：
```python
import time
import asyncio
from fastapi import FastAPI
from uvicorn.main import run

app = FastAPI()


@app.get("/async_slowest")
async def async_slowest():
    # 异步模式但使用了同步的sleep。
    time.sleep(1)
    return {"message": "async mode but use sync sleep"}


@app.get("/async_sleep")
async def async_sleep():
    # 异步模式的sleep
    await asyncio.sleep(1)
    return {"message": "async mode sleep"}


@app.get("/sync")
def sync_sleep():
    # 同步模式的sleep，fastapi会用线程去解决。线程数量 = 计算机cpu核心数 * 5
    time.sleep(1)
    return {"message": "sync, but run in thread pool"}


if __name__ == '__main__':
    run(app='tests.test_003_sleep:app', host='127.0.0.1', port=8001, reload=True)
```

运行代码：```python -m tests.test003_sleep```

### 二，使用压测工具siege，得到如下结果：
```bash
hu@iMac  ~  siege -c 100 -r 1 http://127.0.0.1:8001/async_slowest

{	"transactions":			         100,
 "availability":			      100.00,
 "elapsed_time":			      100.47,
 "data_transferred":		        0.00,
 "response_time":		       98.50,
 "transaction_rate":		        1.00,
 "throughput":			        0.00,
 "concurrency":			       98.03,
 "successful_transactions":	         100,
 "failed_transactions":		           0,
 "longest_transaction":		      100.47,
 "shortest_transaction":		        2.02
}
hu@iMac  ~  siege -c 100 -r 1 http://127.0.0.1:8001/async_sleep

{	"transactions":			         100,
 "availability":			      100.00,
 "elapsed_time":			        1.03,
 "data_transferred":		        0.00,
 "response_time":		        1.03,
 "transaction_rate":		       97.09,
 "throughput":			        0.00,
 "concurrency":			       99.71,
 "successful_transactions":	         100,
 "failed_transactions":		           0,
 "longest_transaction":		        1.03,
 "shortest_transaction":		        1.01
}
hu@iMac  ~  siege -c 100 -r 1 http://127.0.0.1:8001/sync

{	"transactions":			         100,
 "availability":			      100.00,
 "elapsed_time":			        4.03,
 "data_transferred":		        0.00,
 "response_time":		        2.22,
 "transaction_rate":		       24.81,
 "throughput":			        0.00,
 "concurrency":			       55.07,
 "successful_transactions":	         100,
 "failed_transactions":		           0,
 "longest_transaction":		        4.03,
 "shortest_transaction":		        1.01
}
```
其中：
  - 第一种完全是串行处理，100个请求共花费100.47秒。
  - 第二种使用异步sleep，1.03秒内处理了100个请求。
  - 第三种函数使用同步写法，但却仅花费了4.03秒。

第一种和第二种很好理解，但第三种的耗时只有4.03秒，这就是fastapi精彩的地方。前面提到，async函数会放到event loop中执行。 那么，普通的函数会放到哪里呢？答案是，放到thread pool中。

从日志中也观察到server每次处理30个请求（测试机器为6核心），线程池的默认配置是核数*5，所以是30线程，服务器处理100请求则需要至少4秒的时间。

就像官方所说，如果你不清楚你函数里的调用是否异步，那就定义为普通函数。因为它可以采用多线程的方式解决。
反之，定义了async函数，里面却是同步的调用（第一个函数），那么这慢的将是灾难！
