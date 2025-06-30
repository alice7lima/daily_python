from classes.csv_processor import CsvProcessor

if __name__ == '__main__':
    csv_path = 'data/exemplo.csv'
    state = 'DF'
    processor = CsvProcessor(csv_path=csv_path)

    filtered_df = processor.process(state_name=state)
    print(filtered_df)