import asyncio
from aiohttp import ClientSession

async def main():
    async with ClientSession() as aiohttpsession:
        pass

asyncio.run(main())
