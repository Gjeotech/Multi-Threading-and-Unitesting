#Multi Thtreading task

# import threading
# import time
#
# def worker(name):
#     print(f"Thread {name} starting")
#     time.sleep(10)
#     print(f"Thread {name} finished")
#
# thread1 = threading.Thread(target=worker, args=("A",))
# thread2 = threading.Thread(target=worker, args=("B",))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Both threads completed")
#
#


import threading
import time

def staff(name):
    print(f'Thread {name} Started')
    time.sleep(5)
    print(f'Thread {name} Finished')

thread1 = threading.Thread(target=staff, args=("Junior_Staff1",))
thread2 = threading.Thread(target=staff, args=("Junior_Staff2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both Threading completed successfully")

"""
🧪 Topic	🛠️ Mini Project Idea
Threading	Simulate multiple file downloads
Asyncio	Async web scraper or countdown timers
Synchronization	Bank account simulation (thread-safe)
aiohttp (async HTTP)	Fetch data from multiple websites
Thread + Async Combo	GUI app that uses async in background


"""