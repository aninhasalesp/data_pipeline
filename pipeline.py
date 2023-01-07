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
