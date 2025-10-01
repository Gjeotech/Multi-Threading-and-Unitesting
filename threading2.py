#Aysch threading task

# import asyncio
#
# async def worker(name):
#     print(f"Worker {name} starting")
#     await asyncio.sleep(5)
#     print(f"Worker {name} finished")
#
# async def task():
#     task1 = asyncio.create_task(worker("A"))
#     task2 = asyncio.create_task(worker("B"))
#
#     await task1
#     await task2
#
# asyncio.run(task())
#
# print("Both threads completed")



import asyncio

async def ferchTask(name):
    print(f'{name} Started')
    await asyncio.sleep(8)
    print(f'{name} Ended')


async def task():
    taskA = asyncio.create_task(ferchTask('Initial_Fetch'))
    taskB = asyncio.create_task(ferchTask('Second_Fetch'))

    await taskA
    await taskB

asyncio.run(task())

print('Both threading completed successfully')


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