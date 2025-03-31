import requests
from datetime import datetime, timedelta
import pytz
import time

# Replace with the actual NORAD IDs for WaratahSeed-1 and CUAVA-2
WS1_NORAD_ID = "60469"   
C2_NORAD_ID = "60527"         

# CelesTrak API URL for TLE data
CELESTRAK_TLE_URL = "https://celestrak.com/NORAD/elements/gp.php?CATNR={}"

# Function to fetch TLE data for a satellite
def fetch_tle(norad_id):
    response = requests.get(CELESTRAK_TLE_URL.format(norad_id))
    if response.status_code == 200:
        return response.text.strip()
    else:
        raise Exception(f"Failed to fetch TLE for NORAD ID {norad_id}: {response.status_code}")

# Function to write TLE data to a file
def write_tle_to_file(filename, tle_data):
    with open(filename, "w") as file:
        file.write(tle_data)

def record_tle():
    # Sydney timezone
    sydney_tz = pytz.timezone("Australia/Sydney")

    # Define the target times (10 AM and 10 PM) with a 5-minute offset
    target_times = [10, 22]  # 10 AM and 10 PM in 24-hour format

    while True:
        # Get the current time in Sydney timezone
        now = datetime.now(sydney_tz)

        # Check if the current time is within the offset range before the target hour
        for target_hour in target_times:
            target_time = now.replace(hour=target_hour, minute=0, second=0, microsecond=0) 
            if target_time <= now < target_time + timedelta(minutes=1):  # Execute within the 1-minute window
                today = now.date()
                time_str = now.strftime("%H-%M")
                filename = f"{today}_{time_str}.txt"

                try:
                    # Fetch TLE data for both satellites
                    waratahseed_1_tle = fetch_tle(WS1_NORAD_ID)
                    cuava_2_tle = fetch_tle(C2_NORAD_ID)

                    # Combine the TLE data
                    tle_data = f"{waratahseed_1_tle}\n\n{cuava_2_tle}\n"

                    # Write the TLE data to the file
                    write_tle_to_file(filename, tle_data)

                    print(f"TLE data written to {filename}")
                except Exception as e:
                    print(f"Error: {e}")

                # Sleep for 60 seconds to avoid running multiple times within the same minute
                time.sleep(60)
                break
        else:
            # Sleep for a short interval before checking again
            time.sleep(30)

if __name__ == "__main__":
    record_tle()