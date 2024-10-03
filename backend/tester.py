from TikTokApi import TikTokApi
import asyncio
import os
import json
import requests


ms_token = os.environ.get(
    "2HnGfjGxqM7W5lfaePYvgbRQxZCNm2iEl6EYxq99e4-QleqAeIRw9m0CoPkGMyVkT-Xv8s8Ar0muA9yHfgVhD4i3RhhN8-4n0GLn2nbkUgD2quOGUv57odujqstxrlEroulDww9aHcFST9iyXU2ogGs=", None
)  # set your own ms_token, think it might need to have visited a profile


async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        user = api.user("therock")
        user_data = await user.info()
        print(user_data)
        print(ms_token)

        async for video in user.videos(count=10):
            print("-----")
            print(video.id)
            print(video.author.username)
            print(video.as_dict)
            print(video.author.username)
            # URL = "http://192.168.1.88:8217/tiktok-scraper/v1/test/get/title?type=Sexy Girl"
            # DATA = video.as_dict
            #
            # ID_VIDEO = video.id
            # AUTHOR = video.author.username
            # PARAMS = {'id':ID_VIDEO, 'author':AUTHOR}
            # r = requests.post(url = URL,json=DATA)
            # data = r.json()
            # print(data)


if __name__ == "__main__":
        asyncio.run(user_example())
