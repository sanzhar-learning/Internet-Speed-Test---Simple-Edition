import speedtest
from datetime import datetime
from data_utils import save_to_csv
from location_utils import get_location


class UserRecord:

    def __init__(self, username: str):
        self.username = username
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class SpeedTestService:

    def __init__(self):
        self.tester = speedtest.Speedtest()

    def bytes_to_mb(self, bits: float):
        size = round(bits / (8 * 1024 * 1024), 2)
        return f"{size} MBps"

    def run_test(self):
        print("Getting download speed...")
        download_speed = self.tester.download()

        print("Getting upload speed...")
        upload_speed = self.tester.upload()

        print("Getting your ping...")
        ping = self.tester.results.ping

        return download_speed, upload_speed, ping

    def get_location(self):
        print("Getting your location...")
        return get_location()


def run_speed_test():
    print("Hello, user! This is Internet Speed Test by Sanzhar Tashbenbetov.")
    username = input("Please enter your name: ")

    user_record = UserRecord(username)

    user_prompt = input("Type 'start' to start measuring: ")
    while user_prompt != "start":
        print("Error! Please type 'start' to start measuring.")
        user_prompt = input("Type 'start' to start measuring: ")

    speed_service = SpeedTestService()

    download_speed, upload_speed, ping = speed_service.run_test()
    location = speed_service.get_location()

    download_text = speed_service.bytes_to_mb(download_speed)
    upload_text = speed_service.bytes_to_mb(upload_speed)

    print("\nRESULTS:")
    print("Your username:", user_record.username)
    print("Timestamp:", user_record.timestamp)
    print("Your download speed is:", download_text)
    print("Your upload speed is:", upload_text)
    print("Your ping is:", ping, "ms")
    print("Your city is:", location["city"])
    print("Your country is:", location["country"])

    row = {
        "username": user_record.username,
        "timestamp": user_record.timestamp,
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
