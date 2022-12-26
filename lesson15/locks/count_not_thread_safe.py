# run in colab

from threading import Thread

def count(counter_l):
    for i in range(100_000):
        for i in range(len(counter_l)):
            counter_l[i] += 1


if __name__ == '__main__':
    threads = []
    counter_wrapper = [0]

    for i in range(10):
        threads.append(Thread(target=count, args=(counter_wrapper, )))
        threads[-1].start()

    for t in threads:
        t.join()

    print(counter_wrapper)