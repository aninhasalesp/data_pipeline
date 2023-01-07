import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from pipeline import run as run_pipeline


def test_pipeline() -> None:
    """Test main pipeline"""
    resources_path = str(Path(__file__).parent / "resources")
    with open(f"{resources_path}/dados_tratados.csv", "r") as dados_tratados:
        assert run_pipeline(
            f"{resources_path}/censo_estado.csv",
            f"{resources_path}/rouanet.csv"
        ) == dados_tratados.read()
