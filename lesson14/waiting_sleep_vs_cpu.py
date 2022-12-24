import time


def wait_using_sleep(sec):
    print("Counting down")
    time.sleep(sec)
    print(f"{sec} seconds is over")


def wait_wasting_cpu(sec):
    print("Counting down")
    start = time.time()
    while time.time()-start < 5:
        continue
    print(f"{sec} seconds is over")


if __name__ == '__main__':
    wait_using_sleep(45)
    # wait_wasting_cpu(45)