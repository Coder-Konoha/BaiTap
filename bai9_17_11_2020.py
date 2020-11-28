import os
import time

shutdown = input("Bạn có muốn tắt máy (Y/N): ")
if shutdown == "y" or shutdown == "Y":
        print("tat may")
else:
    for i in range(1,30):
        if shutdown == "n" or shutdown == "N":
            for times in range(1, 30):
                time.sleep(0.0000001)
                print(times)
            shutdown = input("Bạn có muốn tắt máy (Y/N): ")
        if shutdown == "y" or shutdown == "Y":
            print("tat may")
            break