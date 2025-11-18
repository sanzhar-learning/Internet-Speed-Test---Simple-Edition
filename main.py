import speedtest
from datetime import datetime
from data_utils import save_to_csv


def bytes_to_mb(bits):
    size = round(bits / (8 * 1024 * 1024), 2)
    return f"{size} MBps"


wifi = speedtest.Speedtest()

print("Hello, user! This is Internet Speed Test by Sanzhar Tashbenbetov (and Valeriy Pokrov).")
username = input("Please enter your name: ")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
flag = False

user_prompt = input("Type 'start' to start measuring: ")

while user_prompt != "start":
    print("Error! Please type 'start' to start measuring.")
    user_prompt = input()

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

save_to_csv(
    "data.csv",
    {
        "username": username,
        "timestamp": timestamp,
        "flag": flag,
        "download_speed_MBps": bytes_to_mb(download_speed),
        "upload_speed_MBps": bytes_to_mb(upload_speed),
        "ping_ms": ping
    }
)
