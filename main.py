import math
import speedtest

def bytes_to_mb(bits):
    size = round(bits / (8 * 1024 * 1024), 2)
    return f"{size} Mpbs"

wifi = speedtest.Speedtest()
print("Hello, user! This is Internet Speed Test by Sanzhar Tashbenbetov.")
user_prompt = input("Type 'start' to start measuring. ")
if user_prompt == "start":
    print("Getting download speed...")
    download_speed = wifi.download()

    print("Getting upload speed...")
    upload_speed = wifi.upload()

    print("Your download speed is:", bytes_to_mb(download_speed))
    print("Your upload speed is:", bytes_to_mb(upload_speed))
else:
    print("Error! Please type 'start' to start measuring.")