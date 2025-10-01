import asyncio  # the toolbox

async def do_work(name):  # async keyword defines coroutine
    print(f"Working...{name}")
    await asyncio.sleep(4)  # pause without blocking
    print(f"Finished with {name}")

async def work():
    work1 = asyncio.create_task(do_work('Work1'))
    work2 = asyncio.create_task(do_work('Work2'))

    await work1
    await work2

asyncio.run(work())  # run the async function

print('Both Asynchronous threading completed successfully')
