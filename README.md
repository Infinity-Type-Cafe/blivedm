# Blivedm
> 用于 [∞-type Café 暑期学校.](https://infinity-type-cafe.github.io/ntype-cafe-summer-school/) 的Bilibili直播间弹幕消息获取


原项目 [blivedm](https://github.com/xfgryujk/blivedm) 基于WebSocket使用Python获取bilibili直播弹幕。

## 依赖
> `pip install -r requirements.txt`

- Python 3.8+
- aiohttp 3.7.4
- Brotli 1.0.9

## 使用
- [./main.py](./main.py) 适用于获取直播间的弹幕和醒目弹幕消息，运行其即可。
- [./sample.py](./sample.py) 为原项目的demo文件。

将直播间的id加入 [./main.py](./main.py) 中 `TEST_ROOM_IDS = []` 即可。

## License
Copyright (c) 2018 xfgryujk
Copyright (c) 2023 Muqiu Han