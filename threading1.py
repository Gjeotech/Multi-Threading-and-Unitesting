#Multi Thtreading task

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


