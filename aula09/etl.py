import pandas as pd
import os, glob
from timer_decorator import timer_decorator

@timer_decorator
def extrair_dados(diretorio_dados: str, formato: str) -> pd.DataFrame:

    if formato not in ["json", "csv", "xlsx"]:
        raise Exception(
            "Formato dos arquivos de entrada não suportado! Formatos válidos: json, csv e xlsx (excel)"
        )

    arquivos = glob.glob(os.path.join(diretorio_dados, f"*.{formato}"))

    funcao_pandas = {"csv": pd.read_csv, "json": pd.read_json, "xlsx": pd.read_excel}

    if len(arquivos) > 0:

        df_lista = [funcao_pandas[formato](arquivo) for arquivo in arquivos]
        df_total = pd.concat(df_lista, ignore_index=True)

        return df_total

    else:
        raise Exception(
            "O diretório informado está vazio, verifique e tente novamente."
        )

@timer_decorator
def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df["Receita"] = df["Quantidade"] * df["Venda"]
    print(df.head())

    return df

@timer_decorator
def carregar_dados(df: pd.DataFrame, formatos: list) -> None:
    for formato in formatos:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)

        elif formato == "parquet":
            df.to_parquet("dados.parquet", index=False)

@timer_decorator
def pipeline(diretorio_entrada: str, formato_entrada: str, formato_saida: str) -> None:
    dados = extrair_dados(diretorio_entrada, formato=formato_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato_saida)
