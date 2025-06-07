import csv
from typing import List, Dict


def ler_csv(caminho: str) -> list:
    with open(caminho, "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def processar_dados(dados_vendas: List[dict]) -> Dict[str, Dict[str, str]]:
    vendas = {}

    for registro in dados_vendas:
        categoria = registro["Categoria"]
        if categoria not in vendas:
            vendas[categoria] = []

        del registro["Categoria"]
        vendas[categoria].append(registro)

    return vendas


def calcular_total_vendas(
    vendas_categoria: Dict[str, List[Dict[str, str]]],
) -> Dict[str, int]:
    total_por_categoria = {}
    for categoria, vendas in vendas_categoria.items():
        total_por_categoria[categoria] = sum(
            [int(venda["Quantidade"]) * int(venda["Venda"]) for venda in vendas]
        )

    return total_por_categoria


if __name__ == "__main__":
    caminho_csv = "vendas.csv"
    dados_brutos_vendas = ler_csv(caminho=caminho_csv)
    dados_processados_vendas = processar_dados(dados_vendas=dados_brutos_vendas)
    total_vendas_categoria = calcular_total_vendas(
        vendas_categoria=dados_processados_vendas
    )

    print("Total de vendas por categoria:", total_vendas_categoria)
