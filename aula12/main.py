from src.interface.classes.csv_processor import CsvProcessor

csv_path = './exemplo.csv'

processor = CsvProcessor(file_path=csv_path)

processor.load_csv()
print(processor.filter_by(columns=["estado", "preço"], attributes=["SP", "10,50"]))