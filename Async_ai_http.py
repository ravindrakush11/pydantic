import aiohttp
import asyncio

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"Fetching: {url}")
        data = await response.json()
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

asyncio.run(main())
