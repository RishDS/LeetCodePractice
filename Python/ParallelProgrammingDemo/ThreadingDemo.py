# https://www.youtube.com/watch?v=fKl2JW_qrso
# https://realpython.com/intro-to-python-threading/
# https://www.youtube.com/watch?v=FChZP09Ba4E

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# new way to do threading
# The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool.
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # notice how we pass args in a function
    # notice that map runs on an iterator, so it picks up one function call for every item in the list
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

# old way to do threading
threads = []
for _ in range(10):
    # notice how we pass the args is different here
    # notice how these therads are not daemon threads, so the below join statement is not needed
    # read up more here: https://realpython.com/intro-to-python-threading/
    # basically, daemon threads will get force killed if the program exits, if its a "non-daemon" thread, 
    # the main program will implicitly call "join" and wait for thread to finish
    # to create a daemon thread we can do: t = threading.Thread(target=do_something, args=[1.5], daemon=True)
    # if we explicitly call join below for the thread, even daemon threads will be waited to finish
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

# notice how we need to explicitly join the threads
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')