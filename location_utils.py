import requests

def get_location():
    url = "https://ipinfo.io/json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return {
            "ip": "unknown",
            "city": "unknown",
            "region": "unknown",
            "country": "unknown",
            "coordinates": "0,0"
        }

    return {
        "ip": data.get("ip", "unknown"),
        "city": data.get("city", "unknown"),
        "region": data.get("region", "unknown"),
        "country": data.get("country", "unknown"),
        "coordinates": data.get("loc", "0,0"),
    }
