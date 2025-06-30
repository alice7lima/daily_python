import pandas as pd


class CsvProcessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.csv_path)

    def remove_empty_cells(self):
        self.df = self.df.dropna()

    def filter_by_state(self, state_name):
        self.df = self.df[self.df["estado"] == state_name]

    def process(self, state_name):
        self.load_csv()
        self.remove_empty_cells()
        self.filter_by_state(state_name=state_name)

        return self.df
