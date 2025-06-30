from classes.etl import ETLFile

if __name__ == '__main__':
    file_path = 'data/exemplo2.json'
    etl = ETLFile(data_source=file_path, output_file_formats=['csv'])

    etl.execute_etl()