import pandas as pd
import logging


logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


csv_url = (
        "https://raw.githubusercontent.com/mlflow/mlflow/master/tests/datasets/winequality-red.csv"
    )
try:
    data = pd.read_csv(csv_url, sep=";")
except Exception as e:
    logger.exception(
            "Unable to download training & test CSV, check your internet connection. Error: %s", e
        )