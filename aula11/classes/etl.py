import os
from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd


class ETLProcess(ABC):
    def __init__(self, data_source, output_file_format=None):
        self.data_source = data_source
        self.output_file_format = output_file_format

    @abstractmethod
    def extract_data(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data(self, data):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def load_data(self, processed_data):
        raise NotImplementedError(
            "O destino de saída fornecido não é um arquivo. Substitua o método load para lidar com esse tipo de destino."
        )

    def execute_etl(self):
        extracted_data = self.extract_data()
        processed_data = self.transform_data(data=extracted_data)
        self.load_data(processed_data=processed_data)


# uma abordagem mais dinamica
class ETLFile(ETLProcess):
    def __init__(self, data_source, output_file_formats):
        super().__init__(data_source)
        self.output_file_formats = output_file_formats
        self.pandas_extract_method = {
            "csv": pd.read_csv,
            "json": pd.read_json,
            "xlsx": pd.read_excel,
        }

    def extract_data(self):
        file_format = os.path.splitext(self.data_source)[1][1:]
        if file_format not in ["json", "csv", "xlsx"]:
            raise ValueError(
                "Formato de arquivo de entrada não suportado! Formatos válidos: json, csv e xlsx (excel)"
            )

        return self.pandas_extract_method[file_format](self.data_source)

    def transform_data(self, data):
        return data.map(lambda x: x.upper() if isinstance(x, str) else x)

    def load_data(self, processed_data):
        current_date = datetime.now().strftime("%Y-%m-%d")
        output_file_name = f"saida_{current_date}"
        for file_format in self.output_file_formats:
            match file_format:
                case "csv":
                    processed_data.to_csv(f"{output_file_name}.{file_format}", index=False)
                case "parquet":
                    processed_data.to_parquet(f"{output_file_name}.{file_format}", index=False)


class ETLCSV(ETLProcess):
    def extract_data(self):
        return pd.read_csv(self.data_source)

    def transform_data(self, data):
        return data.apply(lambda x: x.upper() if isinstance(x, str) else x)

    def load_data(self, processed_data):
        processed_data.to_csv("output.csv")