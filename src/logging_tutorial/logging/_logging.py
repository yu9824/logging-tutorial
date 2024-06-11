import re
from logging import (
    INFO,
    NOTSET,
    Formatter,
    Handler,
    Logger,
    StreamHandler,
    getLogger,
)


def _get_root_logger_name() -> str:
    return __name__.split(".")[0]


def _get_default_handler() -> Handler:
    formatter = Formatter(
        "%(asctime)s - %(name)s:%(lineno)d[%(levelname)s] - %(message)s",
    )

    handler = StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(NOTSET)
    return handler


default_handler = _get_default_handler()


def _get_root_logger() -> Logger:
    # root_logger = getLogger(_get_root_logger_name())
    root_logger = getLogger(_get_root_logger_name())

    root_logger.addHandler(default_handler)
    root_logger.setLevel(INFO)
    root_logger.propagate = False
    return root_logger


root_logger = _get_root_logger()


def get_logger(name: str) -> Logger:
    _result_logger = re.match(rf"{_get_root_logger_name()}\.(.*)", name)
    if _result_logger:
        return root_logger.getChild(_result_logger.group(1))
    else:
        raise ValueError("You should use '__name__'.")


# TODO: rootをdisable, enableする関数を定義する
