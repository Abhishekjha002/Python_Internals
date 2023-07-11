import concurrent.futures
import threading
import time

start_time = time.perf_counter()


def do_something(second):
    print(f"Sleeping for {second} second!!!")
    time.sleep(second)
    return f"Done Sleeping..{second}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


# all_threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     all_threads.append(t)

# for t in all_threads:
#     t.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# do_something()
# do_something()

end_time = time.perf_counter()

print("Time Taken: ", end_time-start_time)
