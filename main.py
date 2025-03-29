import argparse
from src.processor import DataProcessor, watch_directory

class FlightAnalysisApp:
    def __init__(self):
        self.processor = DataProcessor()

    def process_file(self, file_path: str) -> None:
        """
        Process a single flight data file
        """
        try:
            # Load and clean data
            df = self.processor.load_and_clean_data(file_path)
            
            # Analyze delays
            self.processor.analyze_delays(df)
            
            # Save processed file
            output_path = self.processor.save_processed_data(df, file_path)
            print(f"\nProcessed data saved to: {output_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process flight delay data files')
    parser.add_argument('--file', help='Path to specific CSV file to process')
    parser.add_argument('--watch', help='Directory to watch for new CSV files')
    args = parser.parse_args()

    app = FlightAnalysisApp()

    if args.file:
        # Process specific file
        app.process_file(args.file)
    elif args.watch:
        # Watch directory for new files
        watch_directory(args.watch, app.process_file)
    else:
        print("Please provide either --file or --watch argument")
        print("Example usage:")
        print("  Process single file: python main.py --file data/raw/flights.csv")
        print("  Watch directory: python main.py --watch data/raw")

if __name__ == "__main__":
    main() 