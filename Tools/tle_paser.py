from skyfield.api import EarthSatellite, load, wgs84
from datetime import datetime
import pytz
import os

def read_tle_from_file(filename, satellite_name):
    """Reads TLE data for a specific satellite from a file."""
    filename = os.path.expanduser(filename)
    with open(filename, "r") as file:
        lines = file.readlines()

    # Scan through the file to find the satellite name
    for i in range(len(lines)):
        if lines[i].strip().lower() == satellite_name.lower():
            line1 = lines[i + 1].strip()
            line2 = lines[i + 2].strip()
            return satellite_name, line1, line2

    raise ValueError(f"Satellite '{satellite_name}' not found in the file.")

def convert_tle_to_coordinates(filename, satellite_name):
    """Converts TLE data to X, Y, Z, R, Latitude, and Longitude."""
    # Sydney timezone
    sydney_tz = pytz.timezone("Australia/Sydney")

    # Read TLE data for the specified satellite
    satellite_name, line1, line2 = read_tle_from_file(filename, satellite_name)

    # Load the TLE into a Skyfield EarthSatellite object
    satellite = EarthSatellite(line1, line2, satellite_name)
    ts = load.timescale()

    # Get the current time in Sydney timezone
    now = datetime.now(sydney_tz)
    t = ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Compute the satellite's position
    geocentric = satellite.at(t)
    subpoint = wgs84.subpoint(geocentric)

    # Extract Cartesian coordinates (X, Y, Z) in kilometers
    x, y, z = geocentric.position.km

    # Compute radial distance (R) in kilometers
    r = (x**2 + y**2 + z**2)**0.5

    # Extract latitude and longitude
    latitude = subpoint.latitude.degrees
    longitude = subpoint.longitude.degrees

    # Print the results
    print(f"Satellite: {satellite_name}")
    print(f"Time (Sydney Time): {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"X: {x:.3f} km")
    print(f"Y: {y:.3f} km")
    print(f"Z: {z:.3f} km")
    print(f"R: {r:.3f} km")
    print(f"Latitude: {latitude:.3f}°")
    print(f"Longitude: {longitude:.3f}°")

if __name__ == "__main__":
    # Replace with the path to your TLE file
    relative_path = "../TLE_log/2025-03-31_16-48.txt"

    # Resolve the relative path to an absolute path based on the script's location
    script_dir = os.path.dirname(__file__)
    tle_file = os.path.join(script_dir, relative_path)

    # Define the satellite name to calculate, choose from WARATAH SEED-1 or CUAVA-2
    satellite_name = "WARATAH SEED-1"  # Change this to the desired satellite name
    convert_tle_to_coordinates(tle_file, satellite_name)