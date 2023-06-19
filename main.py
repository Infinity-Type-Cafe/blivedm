# -*- coding: utf-8 -*-
import asyncio
import random
import blivedm

# 直播间ID的取值看直播间URL
TEST_ROOM_IDS = []


class handler(blivedm.BaseHandler):
    "弹幕消息的handler, 这里只捕获弹幕消息和醒目的弹幕, 因为我们不需要多余的信息"

    # 普通弹幕
    async def _on_danmaku(
        self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage
    ):
        print(f"{message.timestamp} | {message.uname} : {message.msg}")

    # 醒目弹幕
    async def _on_super_chat(
        self, client: blivedm.BLiveClient, message: blivedm.SuperChatMessage
    ):
        print(f"[{message.start_time}] | {message.uname} : {message.message}")


async def run():
    room_id = random.choice(TEST_ROOM_IDS)

    # 如果SSL验证失败就把ssl设为False，B站真的有过忘续证书的情况
    client = blivedm.BLiveClient(room_id, ssl=False)
    client.add_handler(handler())

    try:
        print(f"-> 目标直播间 {room_id}")
        client.start()
        await client.join()
    finally:
        await client.stop_and_close()


async def main():
    await run()


if __name__ == "__main__":
    asyncio.run(main())
