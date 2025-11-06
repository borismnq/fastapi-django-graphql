import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)


def getenv(name: str, default: Optional[str] = None) -> str:
    env_value = os.environ.get(name, None)
    if env_value in (None, "**NULL**", "NULL", ""):
        return default
    if env_value.lower() == "false":
        return False
    elif env_value.lower() == "true":
        return True
    return env_value


def getvar(key, default=None, required=True):
    """Retrieves system enviroment variable or makes value replacements
    Returns:
        default: any value if it doesn't exist.
    Logging:
        warn: if `key` hasn't been found
    """
    value = os.environ.get(key, default)
    if value == "**NULL**" and default != value:
        value = default
    if value is None or value == "**NULL**":
        if required:
            logger.debug("%s env variable is missing", key)
            return None
    if value == "True":
        return True
    elif value == "False":
        return False
    return value
