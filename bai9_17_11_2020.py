import os
import time

shutdown = input("Bạn có muốn tắt máy (Y/N): ")
if shutdown == "y" or shutdown == "Y":
    os.system("shutdown /s /t 1")
    exit
else:
    for i in range(1,30):
        if shutdown == "n" or shutdown == "N":
            for times in range(1, 30):
                time.sleep(1)
            shutdown = input("Bạn có muốn tắt máy (Y/N): ")
        if shutdown == "y" or shutdown == "Y":
            os.system("shutdown /s /t 1")
            break