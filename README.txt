TLE Logging Script
===================

Description:
------------
This Python script continuously fetches the TLE (Two-Line Element) data for the WaratahSeed-1 and CUAVA-2 satellites at specific times (10 AM and 10 PM Sydney time). The TLE data is saved to a text file named with the current date and time.

Features:
---------
- Fetches TLE data from the CelesTrak API.
- Records TLE data for WaratahSeed-1 and CUAVA-2 satellites.
- Runs continuously and executes at 10 AM and 10 PM Sydney time.
- Saves TLE data to a file in the format `YYYY-MM-DD_HH-MM.txt`.

Requirements:
-------------
- Python 3.x
- Required Python libraries:
  - `requests`
  - `pytz`

Installation:
-------------
1. Clone or download this repository to your local machine.
2. Install the required Python libraries using pip:
