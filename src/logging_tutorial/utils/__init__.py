"""utils module"""

from ._utils import dummy_func, is_argument, is_installed

# _utils.pyだと、_が入っているのでドキュメント化されない。
# ドキュメント化したい場合は、モジュールメソッドとして登録するため、__all__に入れる。
__all__ = ("is_installed", "dummy_func", "is_argument")

if is_installed("tqdm"):
    from ._tqdm import TqdmToLogger, tqdm_joblib

    __all__ += ("tqdm_joblib", "TqdmToLogger")
