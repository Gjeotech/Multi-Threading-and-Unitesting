# import threading
#
# counter = 0
#
# def increment():
#     global counter
#     for _ in range(1000000):
#         counter += 1
#
# thread1 = threading.Thread(target=increment)
# thread2 = threading.Thread(target=increment)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Counter:", counter)  # ❌ Not always 2,000,000!

import threading

balance = 100
lock = threading.Lock()

def withdraw():
    global balance
    for _ in range(10000):
        with lock:
            if balance > 0:
                balance -= 1

threads = [threading.Thread(target=withdraw) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final balance:", balance)  # ✅ Correct
