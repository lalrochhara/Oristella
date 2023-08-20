import asyncio
from Oristella import bot, app

async def main():
    await bot.stop()
    await app.stop()

asyncio.run(main())
