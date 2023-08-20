#!/bin/bash

# Stop the bots
echo "Stopping bots..."
python3 -c "import asyncio; from Oristella import bot, app; async def main(): await bot.stop(); await app.stop(); asyncio.run(main())"

# Close the aiohttp client session to avoid "Unclosed client session" error
echo "Closing aiohttp client session..."
python3 -c "import asyncio; from aiohttp import ClientSession; async def main(): async with ClientSession() as aiohttpsession: pass; asyncio.run(main())"

echo "Deployment complete"
