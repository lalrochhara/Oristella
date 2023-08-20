#!/bin/bash

# Stop the bots
echo "Stopping bots..."
python3 stop_bots.py

# Close the aiohttp client session to avoid "Unclosed client session" error
echo "Closing aiohttp client session..."
python3 close_session.py

echo "Deployment complete"
