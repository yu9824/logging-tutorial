import io
from logging import INFO, Logger
from types import TracebackType
from typing import Optional

from tqdm.auto import tqdm

from ._utils import is_installed

if is_installed("joblib"):
    import joblib

    class tqdm_joblib:
        """tqdm when using joblib"""

        def __init__(self, pbar: tqdm) -> None:
            self.pbar = pbar

            class TqdmBatchCompletionCallBack(
                joblib.parallel.BatchCompletionCallBack
            ):
                def __call__(self, *args, **kwargs):
                    pbar.update(n=self.batch_size)
                    return super().__call__(*args, **kwargs)

            self.TqdmBatchCompletionCallBack = TqdmBatchCompletionCallBack

        def __enter__(self) -> None:
            self._old_batch_callback = joblib.parallel.BatchCompletionCallBack
            joblib.parallel.BatchCompletionCallBack = (
                self.TqdmBatchCompletionCallBack
            )

        def __exit__(
            self,
            exc_type: Optional[type[Exception]],
            exc_value: Optional[Exception],
            traceback: Optional[TracebackType],
        ) -> None:
            joblib.parallel.BatchCompletionCallBack = self._old_batch_callback
            self.pbar.close()

else:

    class tqdm_joblib:
        def __init__(self, pbar: tqdm) -> None:
            pass

        def __enter__(self) -> None:
            pass

        def __exit__(
            self,
            exc_type: Optional[type[Exception]],
            exc_value: Optional[Exception],
            traceback: Optional[TracebackType],
        ) -> None:
            pass


class TqdmToLogger(io.StringIO):
    """
    Output stream for TQDM which will output to logger module instead of
    the StdOut.

    Examples
    --------
    >>> tqdm(total=100, file=TqdmToLogger(_logger))
    """

    def __init__(self, logger: Logger, level: int = INFO):
        super().__init__()
        self.logger = logger
        self.level = level

    def write(self, buf: str):
        self.buf = "\r" + buf.strip("\n\t ")
        self.logger.log(level=self.level, msg=self.buf)
