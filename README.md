# Flight Delay Data Pipeline

A Python-based data pipeline for processing and analyzing flight delay data. This project automatically processes flight data files, performs basic analysis, and saves the cleaned data.

## Features

- Load and clean flight delay data from CSV files
- Perform basic delay analysis including:
  - Average delays by carrier
  - Top 5 routes with highest delays
  - Monthly delay patterns
- Watch directory for new files and process them automatically
- Save processed data in a structured format

## Project Structure

```
flight_analysis/
│
├── data/
│   ├── raw/          # Place input CSV files here
│   └── processed/    # Cleaned and processed files will be saved here
│
├── src/
│   └── processor.py  # Core processing logic
│
├── main.py          # Main entry point
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Requirements

- Python 3.7+
- pandas
- watchdog

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flight_analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

The script can be used in two ways:

### 1. Process a Single File

```bash
python main.py --file data/raw/flights.csv
```

### 2. Watch Directory for New Files

```bash
python main.py --watch data/raw
```

#### How the Watch Function Works:

1. Start the watcher:
```bash
python main.py --watch data/raw
```

2. The script will display:
```
Watching directory: data/raw
Press Ctrl+C to stop...
```

3. Add new CSV files to the watched directory:
   - Simply copy or move CSV files into the `data/raw` directory
   - The script will automatically detect and process each new file
   - You'll see output like:
```
New file detected: data/raw/new_flights.csv
Loading data from data/raw/new_flights.csv

=== Flight Delay Analysis ===
[analysis results will appear here]

Processed data saved to: data/processed/processed_new_flights.csv
```

4. To stop watching:
   - Press `Ctrl+C` in the terminal
   - You'll see: "Stopping directory watch..."

#### Watch Function Tips:

- Keep the terminal window open while watching
- You can add multiple files while the watcher is running
- Each file will be processed automatically as it's added
- Ensure the CSV files have the correct column format

## Input Data Format

The script expects CSV files with the following columns:
- year
- month
- day
- dep_time
- dep_delay
- arr_time
- arr_delay
- carrier
- tailnum
- flight
- origin
- dest
- air_time
- distance
- hour
- minute

## Output

For each processed file, you'll get:
1. Analysis results in the console showing:
   - Average delays by carrier
   - Top 5 routes with highest delays
   - Monthly delay patterns
2. A processed CSV file in the `data/processed/` directory

## Example Output

=== Flight Delay Analysis ===

Average Delays by Carrier:
         dep_delay  arr_delay
carrier                     
AA           10.5       8.2
DL            8.7       6.9
UA           12.3       9.8

Top 5 Routes with Highest Delays:
origin  dest
JFK     LAX    25.3
ORD     SFO    23.1
ATL     LAX    22.7
JFK     SFO    21.9
BOS     LAX    20.5

## Error Handling

The script includes basic error handling for:
- File not found
- Invalid file formats
- Data processing errors

## Contributing

Feel free to submit issues and enhancement requests!
