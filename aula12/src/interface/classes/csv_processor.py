import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtered = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    def filter_by(self, columns, attributes):
        if len(columns) != len(attributes):
            raise ValueError("O número de colunas e atributos diverge!")
        
        if len(columns) == 0:
            return self.df
        
        current_column = columns[0]
        current_attribute = attributes[0]

        df_filtered = self.df[self.df[current_column] == current_attribute]

        if len(columns) == 1:
            return df_filtered
        else:
            return self.filter_by(columns[1:], attributes[1:])