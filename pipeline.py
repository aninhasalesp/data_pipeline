import pandas as pd

from utils.enum import estados_uf


def run(censo_csv_path: str, rouanet_csv_path: str) -> str:
    """Main pipeline"""
    censo_dataframe = pd.read_csv(censo_csv_path)
    rouanet_dataframe = pd.read_csv(rouanet_csv_path)

    merged_dataframes = pd.merge(
        censo_dataframe, 
        rouanet_dataframe,
        left_on='codigo', 
        right_on='estado_ibge', 
    )
    merged_dataframes.set_index(["estado_ibge", "valor_em_reais"])
    removed_duplicated_dataframe = merged_dataframes.drop_duplicates(
        subset=["estado_ibge", "valor_em_reais"]
    )
    
    cleared_dataframe = removed_duplicated_dataframe.drop(
        removed_duplicated_dataframe[
            (
                removed_duplicated_dataframe.valor_em_reais == 0
            ) | (
                removed_duplicated_dataframe.quantidade == 0
            )
        ].index
    )

    result_dataframe = cleared_dataframe.replace({"estado": estados_uf})
    return result_dataframe.to_csv()


if __name__ == "__main__":
    """runnning pipeline as cli"""
    from argparse import ArgumentParser
    from os import path

    parser = ArgumentParser(prog="Trata dados")
    parser.add_argument("censo_path", help="Caminho do arquivo censo no formato csv")
    parser.add_argument("rouanet_path", help="Caminho do arquivo rouanet no formato csv")
    parser.add_argument(
        "-o", "--output_path",
        required=False,
        help="Caminho do arquivo de saída (opcional)"
    )

    args = parser.parse_args()

    result_csv = run(args.censo_path, args.rouanet_path)

    if output_path := args.output_path:
        if path.isdir(output_path):
            output_path = path.join(output_path, "dados_tratados.csv")
        with open(output_path, "w") as output_file:
            output_file.write(result_csv)
    else:
        print(result_csv)
