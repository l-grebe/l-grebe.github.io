# requests实现多文件传输

### 问题
如何通过一个http请求，上传多组文件，如本地图片，视频，音频，文字等？

### 解决方案
上传代码如下：

```python
#!/usr/bin/env python3
# encoding: utf-8

import requests


def main():
    url = 'http://127.0.0.1:8134/item_explain'
    params = {'username': 'user1', }
    res = requests.post(
        url=url,
        params=params,
        files=[
            ('images', ('123_picture001.png', open('~/Pictures/picture001.png', 'rb'), 'image/png', )),
            ('images', ('338_123.jpeg', open('~/Pictures/123.jpeg', 'rb'), 'image/jpeg', )),
            ('audios', ('234_1234.mp3', open('~/Pictures/1234.mp3', 'rb'), 'audio/mp3', )),
            ('audios', ('234_1234.mp3', open('~/Pictures/1234.mp3', 'rb'), 'audio/mp3', )),
            ('audios', ('234_1234.mp3', open('~/Pictures/1234.mp3', 'rb'), 'audio/mp3', )),
            ('videos', ('554_11111.mp4', open('~/Pictures/11111.mp4', 'rb'), 'video/x-mpg', )),
            ('videos', ('554_11111.mp4', open('~/Pictures/11111.mp4', 'rb'), 'video/x-mpg', )),
            ('text', ('explain_text', '最喜小儿无赖，溪头卧剥莲蓬。')),
        ]
    )
    print(res.content)


if __name__ == '__main__':
     main()
```

tornado服务端代码样例：
```python
#!/usr/bin/env python3
# encoding: utf-8

import os
import oss2
import json
import random
import config
import logging
import tornado.ioloop
import tornado.web
from bson import ObjectId


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class ItemExplainHandler(tornado.web.RequestHandler):
    UPLOAD_FILE_TYPE = ('text', 'images', 'audios', 'videos')

    def post(self):
        logging.info("get req.")
        explain = {
            'text': '',
            'images': [],
            'audios': [],
            'videos': [],
        }
        auth = oss2.Auth(config.get("oss_AccessKeyId"), config.get("oss_AccessKeySecret"))
        bucket = oss2.Bucket(auth, config.get("oss_Address"), config.get("oss_Bucket"))
        tmp_object_id = str(ObjectId())
        tmp_object_id = os.path.join(tmp_object_id[:2], tmp_object_id[2:4], tmp_object_id)
        for file_type, file_list in self.request.files.items():
            assert file_type in self.UPLOAD_FILE_TYPE
            if file_type == self.UPLOAD_FILE_TYPE[0]:
                explain['text'] = str(file_list[0]["body"], encoding='utf-8')
            else:
                for idx, http_file in enumerate(file_list):
                    content_type = http_file['content_type']
                    duration, filename = http_file['filename'].split('_', 1)
                    duration = int(duration)
                    suffix = filename.split('.')[-1]
                    random_num = random.randint(0, 100000000)
                    oss_file_path = 'item_explain/{}-{}-{}-{}.{}'.format(tmp_object_id, random_num, file_type, idx, suffix)
                    oss_file_url = "https://{}/{}".format(config.get("oss_Prefix"), oss_file_path)
                    bucket.put_object(oss_file_path, http_file['body'])
                    bucket.update_object_meta(oss_file_path, {
                        # 加了Content-disposition，浏览器会自动下载。
                        # 'Content-disposition': u'attachment;filename="{}"'.format(filename).encode('utf8'),
                        'Content-Type': content_type,
                    })
                    explain[file_type].append({'duration': duration, 'url': oss_file_url})
                    logging.info("{} {} done.".format(file_type, idx + 1))
        logging.info("explain: {}".format(explain))
        self.write("complete.")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/item_explain", ItemExplainHandler),
    ])


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(process)d [line:%(lineno)4s] %(levelname)s %(message)s',
        datefmt='%Y%m%d %H:%M:%S',
        # filename='/tmp/tornado.log',
        # filemode='a',
    )
    app = make_app()
    app.listen(8888)
    logging.info("start.")
    tornado.ioloop.IOLoop.current().start()
```
