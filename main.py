import speedtest
from datetime import datetime

def bytes_to_mb(bits):
    size = round(bits / (8 * 1024 * 1024), 2)
    return f"{size} MBps"

wifi = speedtest.Speedtest()
print("Hello, user! This is Internet Speed Test by Sanzhar Tashbenbetov (and Valeriy Pokrov).")
print("Please enter your name below.")
username = input()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
flag = False
user_prompt = input("Type 'start' to start measuring. ")
if user_prompt == "start":
    flag = True
    print("Getting download speed...")
    download_speed = wifi.download()

    print("Getting upload speed...")
    upload_speed = wifi.upload()

    print("Getting your ping...")
    ping = wifi.results.ping

    print("Your download speed is:", bytes_to_mb(download_speed))
    print("Your upload speed is:", bytes_to_mb(upload_speed))
    print("Your ping is:", ping)
else:
    print("Error! Please type 'start' to start measuring.")

#store name, timestamp, flag, download, upload, ping to csv