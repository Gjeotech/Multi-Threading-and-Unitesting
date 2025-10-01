
"""
🧪 Topic	🛠️ Mini Project Idea
Threading	Simulate multiple file downloads
Asyncio	Async web scraper or countdown timers
Synchronization	Bank account simulation (thread-safe)
aiohttp (async HTTP)	Fetch data from multiple websites
Thread + Async Combo	GUI app that uses async in background

import asyncio → A module

It gives you access to Python’s asynchronous I/O framework.

It includes things like:

asyncio.run() to run async code

asyncio.sleep() for non-blocking delays

asyncio.create_task() for concurrent tasks

Networking tools, queues, and more

=======================
Keyword/Module	What it is	Purpose
import asyncio	✅ A Python module (library)	Provides tools for writing asynchronous code
async	✅ A Python keyword (syntax)	Used to define an asynchronous function
"""

===============FOR COUNTER THREADING==========
✅ TL;DR
Thing	Explanation
balance = 100	Starting amount
10 threads x 10,000 loops	Tries to subtract many times
if balance > 0:	Only subtracts if money is available
with lock:	Ensures one thread modifies at a time
Final balance = 0	Means exactly 100 safe subtractions ran
