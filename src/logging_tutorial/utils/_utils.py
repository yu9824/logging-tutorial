import pkgutil

# deprecated in python >=3.12
from typing import TypeVar

from logging_tutorial.logging import DEBUG, get_logger

T = TypeVar("T")


PACKAGE_NAMES = {_module.name for _module in pkgutil.iter_modules()}

_logger = get_logger(__name__)
_logger.setLevel(DEBUG)
_logger.debug(_logger)


def is_installed(package_name: str) -> bool:
    """Check if the package is installed.

    Parameters
    ----------
    package_name : str
        package name like `sklearn`

    Returns
    -------
    bool
        if installed, True
    """
    return package_name in PACKAGE_NAMES


def dummy_func(x: T, *args, **kwargs) -> T:
    """dummy function

    Parameters
    ----------
    x : T
        Anything

    Returns
    -------
    T
        same as input
    """
    return x


_logger.debug("debug message")
_logger.info("info message")
_logger.warning("warn message")
_logger.error("error message")
_logger.critical("critical message")
