import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from pipeline import run as run_pipeline


def test_pipeline() -> None:
    """Test main pipeline"""
    with open("resources/dados_tratados.csv", "r") as dados_tratados:
        assert run_pipeline(
            "resources/censo_estado.csv",
            "resources/rouanet.csv"
        ) == dados_tratados.read()
