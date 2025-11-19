import speedtest
from datetime import datetime
from data_utils import save_to_csv
from location_utils import get_location


def bytes_to_mb(bits):
    size = round(bits / (8 * 1024 * 1024), 2)
    return f"{size} MBps"


def run_speed_test():
    wifi = speedtest.Speedtest()

    print("Hello, user! This is Internet Speed Test by Sanzhar Tashbenbetov.")
    username = input("Please enter your name: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_prompt = input("Type 'start' to start measuring: ")
    while user_prompt != "start":
        print("Error! Please type 'start' to start measuring.")
        user_prompt = input()

    print("Getting download speed...")
    download_speed = wifi.download()

    print("Getting upload speed...")
    upload_speed = wifi.upload()

    print("Getting your ping...")
    ping = wifi.results.ping

    print("Getting your location...")
    location = get_location()

    download_text = bytes_to_mb(download_speed)
    upload_text = bytes_to_mb(upload_speed)

    print("RESULTS:")
    print("Your download speed is:", download_text)
    print("Your upload speed is:", upload_text)
    print("Your ping is:", ping, "ms")
    print("Your city is:", location["city"])
    print("Your country is:", location["country"])

    row = {
        "username": username,
        "timestamp": timestamp,
        "download_MBps": download_text,
        "upload_MBps": upload_text,
        "ping_ms": ping,
        "ip": location["ip"],
        "city": location["city"],
        "region": location["region"],
        "country": location["country"],
        "coordinates": location["coordinates"],
    }
    save_to_csv("data.csv", row)

def main():
    run_speed_test()

if __name__ == "__main__":
    main()