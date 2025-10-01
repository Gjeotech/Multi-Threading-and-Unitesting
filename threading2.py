#Asynch threading

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

