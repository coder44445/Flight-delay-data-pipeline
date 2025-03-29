import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class DataProcessor:
    def load_and_clean_data(self, file_path: str) -> pd.DataFrame:
        """
        Load and clean flight delay data
        """
        try:
            # Read the CSV file
            print(f"Loading data from {file_path}")
            df = pd.read_csv(file_path)
            
            # Basic cleaning
            # Create datetime column
            df['date'] = pd.to_datetime(dict(
                year=df['year'],
                month=df['month'],
                day=df['day']
            ))
            
            # Clean delay columns
            df['dep_delay'] = df['dep_delay'].fillna(0)
            df['arr_delay'] = df['arr_delay'].fillna(0)
            
            # Convert text columns to uppercase
            for col in ['carrier', 'origin', 'dest']:
                df[col] = df[col].str.upper()
            
            return df
            
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            raise

    def analyze_delays(self, df: pd.DataFrame) -> None:
        """
        Perform basic delay analysis
        """
        print("\n=== Flight Delay Analysis ===")
        
        # Average delays by carrier
        print("\nAverage Delays by Carrier:")
        carrier_delays = df.groupby('carrier')[['dep_delay', 'arr_delay']].mean()
        print(carrier_delays.round(2))
        
        # Top delayed routes
        print("\nTop 5 Routes with Highest Delays:")
        routes = df.groupby(['origin', 'dest'])['arr_delay'].mean()
        print(routes.nlargest(5).round(2))
        
        # Monthly delays
        print("\nMonthly Average Delays:")
        monthly = df.groupby('month')[['dep_delay', 'arr_delay']].mean()
        print(monthly.round(2))

    def save_processed_data(self, df: pd.DataFrame, input_path: str) -> str:
        """
        Save processed data to output directory
        """
        # Create processed directory if it doesn't exist
        os.makedirs('data/processed', exist_ok=True)
        
        # Generate output filename
        filename = os.path.basename(input_path)
        output_path = os.path.join('data/processed', f'processed_{filename}')
        
        # Save file
        df.to_csv(output_path, index=False)
        return output_path

class FileHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.csv'):
            print(f"\nNew file detected: {event.src_path}")
            # Wait a moment to ensure file is completely written
            time.sleep(1)
            self.callback(event.src_path)

def watch_directory(path: str, callback) -> None:
    """
    Watch directory for new CSV files
    """
    event_handler = FileHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    
    print(f"\nWatching directory: {path}")
    print("Press Ctrl+C to stop...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping directory watch...")
    observer.join() 