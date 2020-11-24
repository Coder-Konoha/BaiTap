import os
import time
s = 30
i = 1
shutdown = input("Bạn có muốn tắt máy (Y/N): ")
if shutdown == "y" or shutdown == "Y" and i == s:
        os.system("shutdown /s /t 1")
while i < s:
    if shutdown == "y" or shutdown == "Y" and i == s:
        os.system("shutdown /s /t 1")
        break
    if shutdown == "n" or shutdown == "N":
        for a in range(i, s):
            time.sleep(1)
        shutdown = input("Bạn có muốn tắt máy (Y/N): ")