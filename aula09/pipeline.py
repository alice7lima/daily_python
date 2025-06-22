from etl import pipeline
from pathlib import Path

if __name__ == "__main__":
    diretorio_raiz = Path(__file__).parent
    diretorio_entrada = diretorio_raiz / "data"
    formato_entrada = "json"
    formato_saida = ["csv", "parquet"]

    pipeline(
        diretorio_entrada=diretorio_entrada,
        formato_entrada=formato_entrada,
        formato_saida=formato_saida,
    )
