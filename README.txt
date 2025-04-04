# TLE Logging and Parsing Tools
This project provides tools for logging and parsing Two-Line Element (TLE) data for satellites. It includes functionality to fetch TLE data from CelesTrak, save it to files, and compute satellite positions based on the TLE data.

## Structure
tle-pass-predictor
├── src
│   ├── main.py        # Main script for fetching TLE data and managing command execution
├── Tools               # Tools
│   └── tle_parser.py       # Utility functions for TLE fetching and time calculations
└── README.md           # Documentation for the project

## Features

- **TLE Logging**: Automatically fetches TLE data for specified satellites at specific times (10 AM and 10 PM) and saves it to the `TLE_log` directory.
- **TLE Parsing**: Reads TLE data from a file, computes the satellite's position, and outputs Cartesian coordinates (X, Y, Z), radial distance (R), latitude, and longitude.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `requests`
  - `pytz`
  - `skyfield`

Install the required libraries using:

```bash
pip install requests pytz skyfield
```

## File Structure

- `main.py`: Handles TLE logging by fetching TLE data for specified satellites and saving it to the `TLE_log` directory.
- `Tools/tle_paser.py`: Parses TLE data from a file and computes satellite positions.

## Usage

### 1. Logging TLE Data

Run the `main.py` script to start logging TLE data:

```bash
python3 main.py (Screen Recommanded, see below)
```

#### Screen
Screen is recommanded to run the threads without interuption

Install Screen: Sudo apt install screen
Start new Screen session: screen -S $name
Detach Screen without ending it: Ctrl-A, D
Resume Screen screen -rx $name

Exit Screen: Ctrl-D or exit

### 2. Parsing TLE Data

Use the `tle_paser.py` script to parse TLE data and compute satellite positions:

```bash
python3 Tools/tle_paser.py
```

- The script prompts for the relative path to a TLE file (e.g., `../TLE_log/2025-03-31_16-48.txt`).
- It computes and prints the satellite's position in Cartesian coordinates (X, Y, Z), radial distance (R), latitude, and longitude.

### Example Output

```plaintext
Satellite: WARATAH SEED-1
Time (Sydney Time): 2025-03-31 16:48:00
X: 1234.567 km
Y: 2345.678 km
Z: 3456.789 km
R: 4567.890 km
Latitude: -33.868°
Longitude: 151.209°
```

## Configuration

- **Satellite Names**: Update the satellite name in `tle_paser.py` to either `WARATAH SEED-1` or `CUAVA-2`.
- **TLE File Path**: Provide the relative path to the TLE file when running `tle_paser.py`.

## Notes

- Ensure the `TLE_log` directory exists or is created automatically by `main.py`.
- The logging script (`main.py`) runs continuously and checks the time every 30 seconds to execute at the target times.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [CelesTrak](https://celestrak.com/) for providing TLE data.
- [Skyfield](https://rhodesmill.org/skyfield/) for satellite position calculations.



 

