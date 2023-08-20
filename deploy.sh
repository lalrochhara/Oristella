#!/bin/bash

# Stop the bots
echo "Stopping bots..."
python3 -c "from Oristella import bot, app; await bot.stop(); await app.stop()"

# Close the aiohttp client session to avoid "Unclosed client session" error
echo "Closing aiohttp client session..."
python3 -c "from aiohttp import ClientSession; aiohttpsession = ClientSession(); aiohttpsession.close()"

echo "Deployment complete"
