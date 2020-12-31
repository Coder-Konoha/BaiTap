import os
import time

shutdown = input("Bạn có muốn tắt máy (Y/N): ")
if shutdown == "y" or shutdown == "Y":
    os.system("shutdown /s /t 1")
else:
    while True:
        if shutdown == "n" or shutdown == "N":
                time.sleep(30)
                shutdown = input("Bạn có muốn tắt máy (Y/N): ")
        if shutdown == "y" or shutdown == "Y":
            os.system("shutdown /s /t 1")
            break