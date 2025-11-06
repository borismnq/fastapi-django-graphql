import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_graphql(graphql_filename: str):
    with open(f"{BASE_DIR}/{graphql_filename}", "r") as graphql_file:
        return graphql_file.read()
