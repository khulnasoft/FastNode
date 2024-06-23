import logging
import inspect
from asgi_correlation_id import CorrelationIdFilter


class CustomLogRecord(logging.LogRecord):
    def __init__(self, *args, **kwargs):
        fast().__init__(*args, **kwargs)

        frame = inspect.currentframe().f_back
        while frame:
            if frame.f_globals['__name__'] != __name__ and frame.f_globals['__name__'] != 'logger':
                break
            frame = frame.f_back

        if frame:
            self.filename = frame.f_code.co_filename
            self.lineno = frame.f_lineno
        else:
            self.filename = "unknown"
            self.lineno = 0


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = fast().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self, logger_name='FastNode', log_level=logging.DEBUG):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(log_level)
            self.logger.makeRecord = self._make_custom_log_record
            self.logger.addFilter(CorrelationIdFilter(default_value='-'))

            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - [%(correlation_id)s] - [%(filename)s:%(lineno)d] - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %Z')

            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    @staticmethod
    def _make_custom_log_record(name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        return CustomLogRecord(name, level, fn, lno, msg, args, exc_info, func=func, extra=extra, sinfo=sinfo)

    def debug(self, message, *args):
        self.logger.debug(message)
        if len(args) > 0:
            self.logger.debug(*args)

    def info(self, message, *args):
        self.logger.info(message)
        if len(args) > 0:
            self.logger.info(*args)

    def warning(self, message, *args):
        self.logger.warning(message)
        if len(args) > 0:
            self.logger.warning(*args)

    def error(self, message, *args):
        self.logger.error(message)
        if len(args) > 0:
            self.logger.error(*args)

    def critical(self, message, *args):
        self.logger.critical(message)
        if len(args) > 0:
            self.logger.critical(*args)


logger = Logger('FastNode')

